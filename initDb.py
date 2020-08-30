import pymongo
from config import  mongoUri

if __name__=='__main__':
  client = pymongo.MongoClient(mongoUri, connectTimeoutMS=50000)
  database = client.zomentum
  ticketsCollection = database.tickets
  moviesCollection = database.movies
  try:
    # using TTL of 9000 seconds since IST is ahead by 5.5 hours and we have to delete it after 8 hours
    # 8 hours from utc = 2.5 hours from IST
    ticketsCollection.create_index('showTime', expireAfterSeconds=9000)
    print("TTL index for Tickets created successfully!")
  except Exception as err:
    print(err)

  try:
    # using TTL of 9000 seconds since IST is ahead by 5.5 hours and we have to delete it after 8 hours
    # 8 hours from utc = 2.5 hours from IST
    moviesCollection.create_index('showTime', expireAfterSeconds=9000)
    print("TTL index for Movies created successfully!")
  except Exception as err:
    print(err)
