from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField,TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email,Length
import email_validator



#CONTACT FORM
class ContactForm(FlaskForm):
    name = StringField("お名前",validators=[DataRequired(message='名前を入力してください')])
    email = StringField('メールアドレス',validators=[DataRequired(message='メールアドレスを入力してください'),Length(max=60), validators.Email(message='正しいメールアドレスを入力してください')])
    subject = StringField('会社名')
    message = TextAreaField('お問合せ内容',validators=[DataRequired(message='お問あわせ内容を入力してください')])
    submit = SubmitField('送信する')


# #REFISTRATION FORM
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')