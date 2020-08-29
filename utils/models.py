from flask_restx import fields, reqparse

class RequestModels:

  def __init__(self, api):
    self.api = api

  def BookTicketModel(self):
    return self.api.model('Ticket', {
      'phoneNumber': fields.Integer('Phone number.'),
      'userName': fields.String('User Name'),
      'timestamp': fields.String('Timing of show as timestamp')
    })

  def UpdateTimingModel(self):
    return self.api.model('UpdateTiming', {
      'currentTime': fields.String("Timestamp of current show timing"),
      'newTime': fields.String("Timestamp of new show timing")
      })

  # GET Methods parser models

  def ViewAllTicketModel(self):
    model = reqparse.RequestParser()
    model.add_argument('movieId', help='Unique Movie ID', required=True)
    return model
  
  def UserDetailsModel(self):
    model = reqparse.RequestParser()
    model.add_argument('ticketId', help='Unique Ticket ID', required=True)
    return model


  def DeleteTicketModel(self):
    return self.api.model('DeleteTicket', {
    'ticketId': fields.String('Unique ID of Ticket')
    })

  def MarkTicketExpireModel(self):
    return self.api.model('MarkExpire', {
    'ticketId': fields.String('Unique ID of Ticket')
    })