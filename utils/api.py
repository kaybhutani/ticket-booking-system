from flask_restx import (
  Api,
  fields,
  Namespace,
  Resource
)

# set apiAuth to False if you want to test without auth-token
apiAuth = False
xAuthToken = '123xyz'

api = Namespace('api', description='Booking and Tickets related methods.')


bookTicketModel = api.model('Ticket', {'phoneNumber': fields.Integer('Phone number.'), 'userName': fields.String('User Name'), 'timestamp': fields.String('Timing of show as timestamp')})
UpdateTimingModel = api.model('UpdateTiming', {'currentTime': fields.String("Timestamp of current show timing"), 'newTime': fields.String("Timestamp of new show timing")})
ViewAllTicketModel = api.model('ViewAllTickets', {'movieId': fields.String('Unique ID of Movie')})
DeleteTicketModel = api.model('DeleteTicket', {'ticketId': fields.String('Unique ID of Ticket')})
UserDetailsModel = api.model('UserDetails', {'ticketId': fields.String('Unique ID of Ticket')})
MarkTicketExpireModel = api.model('MarkExpire', {'ticketId': fields.String('Unique ID of Ticket')})

@api.route('/book-ticket')
class BookTicket(Resource):

  @api.expect(bookTicketModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/update-timing')
class UpdateTiming(Resource):

  @api.expect(UpdateTimingModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200


@api.route('/view-all-tickets')
class ViewAllTickets(Resource):

  @api.expect(ViewAllTicketModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/delete-ticket')
class DeleteTicket(Resource):

  @api.expect(DeleteTicketModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/user-details')
class DeleteTicket(Resource):

  @api.expect(UserDetailsModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

@api.route('/mark-expire')
class MarkTicketExpire(Resource):

  @api.expect(MarkTicketExpireModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200
