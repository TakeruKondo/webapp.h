from flask import Flask, render_template,url_for,request, redirect
from flask_login import login_user, logout_user, current_user, login_required
from CAPP.contact.forms import ContactForm
from flask_mail import Mail,Message 
from CAPP.contact.config import mail_username, mail_password


