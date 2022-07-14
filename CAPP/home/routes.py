from flask import Blueprint,render_template

home = Blueprint('home',__name__,template_folder="templates", static_folder="static")


@home.route('/')
def my_home():
    return render_template('index.html')

@home.route('/index.html')
def aboutus():
    return render_template('/index.html')

@home.route('/blog.html')
def blog():
    return render_template('index.html')
