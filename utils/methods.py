from utils.database import CreateDatabaseClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import dateutil.parser

client = CreateDatabaseClient()
moviesCollection = client.moviesCollection()
ticketsCollection = client.ticketsCollection()


def bookTicket(jsonData):
  showTimeString = jsonData.get('showTime')
  if not (jsonData.get('phoneNumber') and jsonData.get('userName')):
    return
  try:
    showTime = dateutil.parser.parse(showTimeString)
    if showTime < datetime.utcnow() + timedelta(hours=5.5):  # converting to IST Time
      return {'succes': False, 'message': 'Show time cannot be before current time.'}, 400
  except Exception as err:
    return {'success': False, 'message': str(err)}, 401

  result = moviesCollection.find_one({'showTime': showTime})
  if not result:
    moviesCollection.insert_one({"showTime": showTime, 'ticketCount': 0})
    result = moviesCollection.find_one({'showTime': showTime})
  newTicketCount = result.get('ticketCount') + jsonData.get('ticketCount')
  if newTicketCount > 20:
    return {'success': False, 'message': 'Ticket limit exceeded.'}, 201

  jsonData['movieId'] = result['_id']
  jsonData['showTime'] = showTime
  response = ticketsCollection.insert_one(jsonData)

  # updating count of sold tickets
  moviesCollection.update_one({"_id": result['_id']}, {"$set": {
    "ticketCount": newTicketCount
  }})
  jsonData['movieId'] = str(jsonData['movieId'])
  jsonData['ticketId'] = str(response.inserted_id)
  jsonData.pop('_id')
  jsonData['showTime'] = str(showTime)
  return {'success': True, 'data': jsonData}


def deleteTicket(jsonData):
  ticketId = jsonData.get('ticketId')
  if not ObjectId.is_valid(ticketId):
    return {'success': False, 'message': 'Ticket ID is not valid.'}, 401
  res = ticketsCollection.find_one({'_id': ObjectId(ticketId)})
  if not res:
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 404
  ticketsCollection.delete_one({'_id': ObjectId(ticketId)})
  moviesCollection.update_one({'_id': ObjectId(res['movieId'])}, {"$inc": {
    "ticketCount": -res['ticketCount']
  }})

  return {'success': True, 'message': 'Ticket Successfully deleted'}


def getUserDetails(ticketId):
  if not ObjectId.is_valid(ticketId):
    return {'success': False, 'message': 'Ticket ID is not valid.'}, 401
  res = ticketsCollection.find_one({'_id': ObjectId(ticketId)})

  if not res:
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 404
  res.pop('_id')
  res.pop('movieId')
  res.pop('ticketCount')
  res.pop('showTime')
  return {'success': True, 'userDetails': res}, 200


def getAllTickets(movieId, showTimeString):
  if showTimeString:
    try:
      showTime = dateutil.parser.parse(showTimeString)
    except Exception as err:
      return {'success': False, 'message': str(err)}, 401
    res = moviesCollection.find_one({'showTime': showTime})
    allTickets = list(ticketsCollection.find({'showTime': showTime}))
  else:
    if not ObjectId.is_valid(movieId):
      return {'success': False, 'message': 'Movie ID is not valid.'}, 401
    res = moviesCollection.find_one({'_id': ObjectId(movieId)})

    if not res:
      return {'success': False, 'message': 'Movie ID does not exist in Database.'}, 404
    allTickets = list(ticketsCollection.find({'movieId': ObjectId(movieId)}))

  for ticket in allTickets:
    ticket['ticketId'] = str(ticket['_id'])
    ticket.pop('_id')
    ticket['movieId'] = str(ticket['movieId'])
    ticket.pop('showTime')
    ticket.pop('movieId')

  if not res:
    return {'success': False, 'message': 'Could not find a movie that match provided details.'}, 404
  return {'success': True, 'movieId': str(res.get('_id')), 'showTime': str(res['showTime']),
          'allTickets': allTickets}, 200


def updateTicket(jsonData):
  showTimeString = jsonData.get('newShowTime')
  try:
    showTime = dateutil.parser.parse(showTimeString)
  except Exception as err:
    return {'success': False, 'message': str(err)}, 401

  ticketId = jsonData.get('ticketId')
  if not ObjectId.is_valid(ticketId):
    return {'success': False, 'message': 'Ticket ID is not valid.'}, 401
  res = ticketsCollection.find_one({'_id': ObjectId(ticketId)})

  if not res:
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 404

  deleteTicket({'ticketId': ticketId})
  res['showTime'] = jsonData['newShowTime']
  res.pop('movieId')
  return bookTicket(res)

