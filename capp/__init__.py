from flask import Flask
from flask_mail import Mail
from capp.config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy



db= SQLAlchemy()
LoginManager=LoginManager()
bcrypt = Bcrypt()


mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    
    mail.init_app(app)

    from .home.routes import home
    from .booking.routes import bookingme
    from .contact.routes import contactme
    from .login.routes import loginme
    from .errors.handlers import errors

    app.register_blueprint(home)
    app.register_blueprint(bookingme)
    app.register_blueprint(contactme)
    app.register_blueprint(loginme)
    app.register_blueprint(errors)

    return app