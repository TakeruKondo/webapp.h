from flask import Blueprint,render_template

bookingme = Blueprint('bookingme',__name__,template_folder="templates",static_folder="static")


@bookingme.route('/booking.html')
def booking():
    return render_template('booking.html')

