from flask import Flask
from flask_mail import Mail
from capp.config import Config


mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mail.init_app(app)

    from .home.routes import home
    from .booking.routes import bookingme
    from .contact.routes import contactme
    from .login.routes import loginme

    app.register_blueprint(home)
    app.register_blueprint(bookingme)
    app.register_blueprint(contactme)
    app.register_blueprint(loginme)

    return app