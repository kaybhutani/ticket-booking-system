from flask import (
  Flask
)
from flask_restx import (
  Api,
  Namespace
)
# import api namespace and all endpoints
from utils.api import api

app = Flask(__name__)

flaskApp = Api(title='Zomentum Assessment - Ticket booking system', description='Made by Kartikay Bhutani\nRoll Number: 9917102214\n\n ### Use the following swagger to test the **API\'s**.\n- Click on the namespace (api).\n- Choose any endpoint you like and click on **Try it out**.\n- You can also see the serializers and Request models in **models**' , version='1.0')
flaskApp.add_namespace(api)
flaskApp.init_app(app)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)