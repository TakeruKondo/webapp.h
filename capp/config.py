import os 


class Config:

    SECRET_KEY = '3246746'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_DEFAULT_SENDER='kond91033@gmail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'kond91033@gmail.com'
    MAIL_PASSWORD = 'uhuspuyhamatjtak'
    MAIL_USE_TLS = False
    MAIL_USE_SSL=True,