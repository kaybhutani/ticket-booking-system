from pymongo import MongoClient
from config import mongoUri


class CreateDatabaseClient:

  def __init__(self):    
    self.client = MongoClient(mongoUri, connectTimeoutMS=50000)
    self.database = self.client.zomentum
  
  def moviesCollection(self):
    return self.database.movies

  def ticketsCollection(self):
    return self.database.tickets
