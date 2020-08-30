import os
import unittest
from app import app
from datetime import datetime, timedelta

class ApiTest(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    self.app = app.test_client()
    self.assertEqual(app.debug, False)


  def test_book_ticket(self):
    payload = {'userName': 'test', 'phoneNumber': '9999999999', 'ticketCount': 5,
               'showTime': str(datetime.now() + timedelta(hours=5.5))}
    response = self.app.post('/api/book-ticket', json=payload)
    self.assertEqual(response.status_code, 200)
    self.testMovieId = response.json['data']['movieId']
    self.testTicketId = response.json['data']['ticketId']

  def test_user_details(self):
    response = self.app.get('/api/user-details', query_string=dict(ticketId='5f4c0d83e24004e8adad2f5c'))
    print(response.json)
    self.assertEqual(response.status_code, 200)

  def test_all_tickets(self):
    response = self.app.get('/api/view-all-tickets', query_string=dict(movieId='5f4c0d82e24004e8adad2f5b'))
    print(response.json)
    self.assertEqual(response.status_code, 200)

  def test_update_time(self):
    response = self.app.put('/api/update-timing', json=dict(ticketId='5f4c0d83e24004e8adad2f5c', newShowTime=str(datetime.now() + timedelta(hours=5.5))))
    print(response.json)
    self.assertEqual(response.status_code, 200)

  # uncomment to test delete_ticket method, Will delete TEST ticket from Database.

  # def test_delete_ticket(self):
  #   response = self.app.delete('/api/delete-ticket', json=dict(ticketId='5f4c0d83e24004e8adad2f5c'))
  #   print(response.json)
  #   self.assertEqual(response.status_code, 200)
if __name__ == "__main__":
  unittest.main()


