from unicodedata import name
from flask import Blueprint,render_template,redirect,request,flash
from .forms import ContactForm
from .utils import send_mail

contactme = Blueprint('contactme',__name__,template_folder="templates", static_folder="static")


@contactme.route('/contact.html', methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_mail('codeit910@yahoo.com','お問い合わせが届きました')
        return redirect('/form_submitted')
    return render_template('contact.html', form=form)


@contactme.route('/form_submitted')
def success():
    return render_template('thankyou.html')