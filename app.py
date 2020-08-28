from flask import (
  Flask,
  request,
  jsonify
)
from flask_restx import (
  Api,
  fields,
  Resource
)

# set apiAuth to False if you want to test without auth-token
apiAuth = False
xAuthToken = '123xyz'

app = Flask(__name__)
api = Api(app)


bookTicketModel = api.model('Ticket', {'phoneNumber': fields.Integer('Phone number.'), 'userName': fields.String('User Name'), 'timestamp': fields.String('Timing of show as timestamp')})


@api.route('/book-ticket')
class BookTicket(Resource):

  @api.expect(bookTicketModel)
  def post(self):
    if apiAuth:
      if not request.headers.get('X-Auth-Token') == xAuthToken:
        return {"success": False, "response": "Invalid Auth token"}, 401
    requestBody = request.get_json()
    print(requestBody)
    return {"success": True}, 200

# @app.route('/book-ticket', methods=['POST'])
# def bookTicket():
#   # check if apiAuth is required and auth token is Valid.
#   if apiAuth:
#     if not request.headers.get('X-Auth-Token') == xAuthToken:
#       return {"success": False, "response": "Invalid Auth token"}

#   requestBody = request.get_json()
#   print(requestBody)
#   return {"success": True}






if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)