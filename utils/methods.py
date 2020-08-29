from utils.database import CreateDatabaseClient

client = CreateDatabaseClient()
moviesCollection = client.moviesCollection()
ticketsCollection = client.ticketsCollection()


def bookTicket(jsonData):
  moviesCollection.insert_one(jsonData)