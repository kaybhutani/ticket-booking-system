from utils.database import CreateDatabaseClient
from bson.objectid import ObjectId

client = CreateDatabaseClient()
moviesCollection = client.moviesCollection()
ticketsCollection = client.ticketsCollection()


def bookTicket(jsonData):
  result = moviesCollection.find_one({'timestamp': jsonData.get('timestamp')})

  if not result:
    moviesCollection.insert_one({"timestamp": jsonData.get('timestamp'), 'ticketCount': 0})
    result = moviesCollection.find_one({'timestamp': jsonData.get('timestamp')})

  newTicketCount = result.get('ticketCount') + jsonData.get('ticketCount')
  print(newTicketCount)
  if newTicketCount > 20:
    return {'success': False, 'message': 'Ticket limit exceeded.'}, 201

  jsonData['movieId'] = result['_id']
  response = ticketsCollection.insert_one(jsonData)
  moviesCollection.update_one({"_id": result['_id']}, {"$set": {
    "ticketCount": newTicketCount
  }})
  jsonData['movieId'] = str(jsonData['movieId'])
  jsonData['ticketId'] = str(response.inserted_id)
  jsonData.pop('_id')
  return {'success': True, 'data': jsonData}


def deleteTicket(jsonData):
  ticketId = jsonData.get('ticketId')
  if not ObjectId.is_valid(ticketId):
    return {'success': False, 'message': 'Ticket ID is not valid.'}, 401
  res = ticketsCollection.find_one({'_id': ObjectId(ticketId)})
  if not res:
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 400
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
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 400
  res.pop('_id')
  res.pop('movieId')
  res.pop('ticketCount')
  res.pop('timestamp')
  return {'success': True, 'userDetails': res}, 200

def getAllTickets(movieId):
  if not ObjectId.is_valid(movieId):
    return {'success': False, 'message': 'Movie ID is not valid.'}, 401
  res = moviesCollection.find_one({'_id': ObjectId(movieId)})

  if not res:
    return {'success': False, 'message': 'Movie ID does not exist in Database.'}, 400
  allTickets = list(ticketsCollection.find({'movieId': ObjectId(movieId)}))

  for ticket in allTickets:
    ticket['ticketId'] = str(ticket['_id'])
    ticket.pop('_id')
    ticket['movieId'] = str(ticket['movieId'])
  return {'success': True, 'allTickets': allTickets}, 200

def updateTicket(jsonData):
  ticketId = jsonData.get('ticketId')
  if not ObjectId.is_valid(ticketId):
    return {'success': False, 'message': 'Ticket ID is not valid.'}, 401
  res = ticketsCollection.find_one({'_id': ObjectId(ticketId)})

  if not res:
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 400

  deleteTicket({'ticketId': ticketId})
  res['timestamp'] = jsonData['newTime']
  res.pop('movieId')
  return  bookTicket(res)
