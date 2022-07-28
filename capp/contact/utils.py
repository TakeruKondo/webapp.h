from flask import render_template, request
from flask_mail import Mail, Message
from capp import mail
from flask import current_app

def send_mail(to, subject):

    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg= Message(subject,recipients=[to])
    msg.html = render_template('maiil-temp1.html', name=name, email = email, subject = subject, message=message)
    mail.send(msg)
