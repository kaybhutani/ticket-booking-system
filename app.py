from flask import (
  Flask,
  request,
  jsonify
)

# set apiAuth to False if you want to test without auth-token
apiAuth = True
xAuthToken = '123xyz'

app = Flask(__name__)

@app.route('/book-ticket', methods=['POST'])
def bookTicket():
  # check if apiAuth is required and auth token is Valid.
  if apiAuth:
    if not request.headers.get('X-Auth-Token') == xAuthToken:
      return {"success": False, "response": "Invalid Auth token"}
  
  requestBody = request.get_json()
  print(requestBody)
  return {"success": True}


if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)