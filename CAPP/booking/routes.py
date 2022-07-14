from flask import Blueprint,render_template

booking = Blueprint('booking',__name__,template_folder="templates",static_folder="static")


@booking.route('/booking.html')
def booking():
    return render_template('booking.html')

