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
    response = self.app.get('/api/user-details', query_string=dict(ticketId='5f4bce71f5e7364a94a2f97f'))
    print(response.json)
    self.assertEqual(response.status_code, 200)

  def test_all_tickets(self):
    response = self.app.get('/api/view-all-tickets', query_string=dict(movieId='5f4bbc04f5ce1f47ceaf2155'))
    print(response.json)
    self.assertEqual(response.status_code, 200)

  def test_update_time(self):
    response = self.app.put('/api/update-timing', json=dict(ticketId='5f4bce71f5e7364a94a2f97f', newShowTime=str(datetime.now() + timedelta(hours=5.5))))
    print(response.json)
    self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
  unittest.main()


