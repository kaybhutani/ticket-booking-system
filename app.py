from flask import (
  Flask
)
from flask_restx import (
  Api,
  Namespace
)
# import api namespace and all endpoints
from utils import api

app = Flask(__name__)

flaskApp = Api(title='Zomentum Assessment - Ticket booking system', version='1.0')
flaskApp.add_namespace(api.api)
flaskApp.init_app(app)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)