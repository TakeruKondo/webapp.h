from email import policy
from flask import Blueprint,render_template,redirect,request,url_for,flash
from capp import db, bcrypt
from capp.models import User
from .login_form import LoginForm,RegistrationForm, RequestResetForm
# from flask_login import login_user, current_user, logout_user, login_required

loginme = Blueprint('loginme',__name__,template_folder="templates", static_folder="static")

@loginme.route('/register.html',methods=['GET','POST'])
def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('user_home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.create_all()
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for('loginme.login'))
    return render_template('register.html', form=form)



@loginme.route('/login.html', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('user_home'))
    form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('user_home'))
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',form=form)


# @loginme.route('/logout.html')
# def logout():
#     logout_user()
#     return redirect(url_for('home'))



# @loginme.route("/account")
# @login_required
# def account():
#     return render_template('account.html', title='Account')


@loginme.route('/policy.html')
def policy():
    return render_template('policy.html')




@loginme.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    # if current_user.is_authenticated:
    #     return redirect(url_for('main.home'))
    form = RequestResetForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     send_reset_email(user)
    #     flash('An email has been sent with instructions to reset your password.', 'info')
    #     return redirect(url_for('users.login'))
    return render_template('reset_request.html', form=form)