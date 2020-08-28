from flask_restx import fields

bookTicketModel = api.model('Ticket', {
    'phoneNumber': fields.Integer('Phone number.'),
    'userName': fields.String('User Name'),
    'timestamp': fields.String('Timing of show as timestamp')
  })

UpdateTimingModel = api.model('UpdateTiming', {
  'currentTime': fields.String("Timestamp of current show timing"),
  'newTime': fields.String("Timestamp of new show timing")
  })

ViewAllTicketModel = api.model('ViewAllTickets', {
  'movieId': fields.String('Unique ID of Movie')
  })

DeleteTicketModel = api.model('DeleteTicket', {
  'ticketId': fields.String('Unique ID of Ticket')
  })

UserDetailsModel = api.model('UserDetails', {
  'ticketId': fields.String('Unique ID of Ticket')
  })

MarkTicketExpireModel = api.model('MarkExpire', {
  'ticketId': fields.String('Unique ID of Ticket')
  })
z