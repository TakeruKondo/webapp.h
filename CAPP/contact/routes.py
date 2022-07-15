from flask import Blueprint,render_template,redirect,request
from .forms import ContactForm
from .utils import send_mail

contactme = Blueprint('contactme',__name__,template_folder="templates", static_folder="static")


@contactme.route('/contact.html', methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # print('-------------------------')
        # print(request.form['name'])
        # print(request.form['email'])
        # print(request.form['subject'])
        # print(request.form['message'])       
        # print('-------------------------')
        
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
            
        
        send_mail('codeit910@yahoo.com','お問い合わせ',"<b>testing</b>")
        return redirect('/form_submitted')

    return render_template('contact.html', form=form)


@contactme.route('/form_submitted')
def success():
    return render_template('thankyou.html')