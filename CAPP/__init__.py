from flask import Flask

from home.routes import home
from booking.routes import booking
from contact.routes import contactme
from login.routes import loginme



def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)
    app.register_blueprint_(booking)
    app.register_blueprint(contactme)
    app.register_blueprint(loginme)

    return app