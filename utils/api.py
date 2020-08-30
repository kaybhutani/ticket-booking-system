from flask import (
  request
)

from flask_restx import (
  Namespace,
  Resource,
)

from utils.models import RequestModels
from config import apiAuth, xAuthToken
from utils.methods import bookTicket, deleteTicket, getAllTickets, getUserDetails, updateTicket

api = Namespace('api', description='Booking and Tickets related methods.')

# importing all request models
RequestModel = RequestModels(api)
BookTicketModel = RequestModel.BookTicketModel()
UpdateTimingModel = RequestModel.UpdateTimingModel()
ViewAllTicketModel = RequestModel.ViewAllTicketModel()
UserDetailsModel = RequestModel.UserDetailsModel()
DeleteTicketModel = RequestModel.DeleteTicketModel()


@api.route('/book-ticket')
class BookTicket(Resource):

  @api.expect(BookTicketModel)
  def post(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    response = bookTicket(requestBody)
    return response


@api.route('/update-timing')
class UpdateTiming(Resource):

  @api.expect(UpdateTimingModel)
  def put(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    return updateTicket(requestBody)


@api.route('/view-all-tickets')
class ViewAllTickets(Resource):

  @api.expect(ViewAllTicketModel)
  def get(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    movieId = ViewAllTicketModel.parse_args().get('movieId')
    showTime = ViewAllTicketModel.parse_args().get('showTime')

    if not movieId and not showTime:
      return {'success': False, 'message': 'Please pass one of the params (movieId or showTime)'}, 401
    return getAllTickets(movieId, showTime)


@api.route('/delete-ticket')
class DeleteTicket(Resource):

  @api.expect(DeleteTicketModel)
  def delete(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    requestBody = request.get_json()
    return deleteTicket(requestBody)


@api.route('/user-details')
class UserDetails(Resource):

  @api.expect(UserDetailsModel)
  def get(self):
    # executed only if apiAuth is set True
    # checks for Api key (X-Auth-Token in header)
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401

    ticketId = UserDetailsModel.parse_args()['ticketId']
    return getUserDetails(ticketId)
