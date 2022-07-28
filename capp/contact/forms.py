from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField,TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email,Length,InputRequired
import email_validator



#CONTACT FORM
class ContactForm(FlaskForm):
    name = StringField("お名前",validators=[InputRequired(message='名前を入力してください')])
    email = StringField('メールアドレス',validators=[InputRequired(message='*メールアドレスを入力してください'),Length(max=60), validators.Email(message='正しいメールアドレスを入力してください')])
    subject = StringField('会社名')
    message = TextAreaField('お問合せ内容',validators=[InputRequired(message='お問あわせ内容を入力してください')])
    submit = SubmitField('送信する')
