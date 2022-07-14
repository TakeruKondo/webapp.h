from flask import Blueprint,render_template,redirect,request

loginme = Blueprint('loginme',__name__,template_folder="templates", static_folder="static")

@loginme.route('/register.html')
def register():
    return render_template('register.html')

@loginme.route('/login.html')
def login():
    return render_template('login.html')