from flask import Blueprint,render_template,redirect,request

contactme = Blueprint('contactme',__name__,template_folder="templates", static_folder="static")


@contactme.route('/contact.html', methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message()
        return redirect('/form_submitted')

    return render_template('contact.html', form=form)


@contactme.route('/form_submitted')
def success():
    return render_template('thankyou.html')

def send_message():
    #get data from form
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # entry = Queries(name=name, email=email, sub=subject, msg=message, date=datetime.datetime.now())
    # db.session.add(entry)
    # db.session.commit()


    msg = Message(
        subject=f"{name} 様からお問合せがありました", body=f"お名前: {name}\n\nEメールアドレス: {email}\n\n会社名: {subject}\n\n\nお問合せ内容: \n\n{message}", sender=mail_username, recipients=['chisato.hahaha.c.h0516@gmail.com']
    )
    mail.send(msg)