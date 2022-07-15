from flask import request
from flask_mail import Mail, Message
from capp import mail
from flask import current_app

def send_mail(to, subject,template):


    msg= Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config["MAIL_DEFAULT_SENDER"]
    )

   
    mail.send(msg)