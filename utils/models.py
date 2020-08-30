from flask_restx import fields, reqparse

class RequestModels:

  def __init__(self, api):
    self.api = api

  def BookTicketModel(self):
    return self.api.model('Ticket', {
      'phoneNumber': fields.Integer('Phone number.'),
      'userName': fields.String('User Name'),
      'ticketCount': fields.Integer('Count of movie tickets to book.'),
      'showTime': fields.String('Timing of show as in ISO format (YYYY-MM-DD HH:MM:SS)')
    })

  def UpdateTimingModel(self):
    return self.api.model('UpdateTiming', {
      'newShowTime': fields.String("New timing of show as in ISO format(YYYY-MM-DD HH:MM:SS)"),
      'ticketId': fields.String("Unique Ticket ID")
      })

  # GET Methods parser models

  def ViewAllTicketModel(self):
    model = reqparse.RequestParser()
    model.add_argument('movieId', help='Unique Movie ID')
    model.add_argument('showTime', help='Show time in ISO format(YYYY-MM-DD HH:MM:SS)')
    return model
  
  def UserDetailsModel(self):
    model = reqparse.RequestParser()
    model.add_argument('ticketId', help='Unique Ticket ID', required=True)
    return model


  def DeleteTicketModel(self):
    return self.api.model('DeleteTicket', {
    'ticketId': fields.String('Unique ID of Ticket')
    })
