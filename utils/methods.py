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

  if newTicketCount >20:
    return {'success': False, 'message': 'Ticket limit exceeded.'},  201

  jsonData['movieId'] = result['_id']
  response = ticketsCollection.insert_one(jsonData)
  moviesCollection.update_one({"_id": result['_id']}, {"$set": {
    "count": newTicketCount
  }})
  jsonData['movieId'] = str(jsonData['movieId'])
  jsonData['_id'] = str(response.inserted_id)
  return {'success': True, 'data': jsonData }

def deleteTicket(jsonData):
  ticketId = jsonData.get('ticketId')
  if len(ticketId)<12:
    return {'success': False, 'message': 'Ticket ID is not valid.'}, 401
  res = ticketsCollection.find_one({'_id': ObjectId(ticketId)})
  if not res:
    return {'success': False, 'message': 'Ticket ID does not exist in Database.'}, 400
  ticketsCollection.delete_one({'_id': ObjectId(ticketId)})
  moviesCollection.update_one({'_id': ObjectId(res['movieId'])}, {"$inc": {
    "count": -res['ticketCount']
  }})

  return {'success': True, 'message': 'Ticket Successfully deleted'}
  