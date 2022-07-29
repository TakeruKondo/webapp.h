from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField,TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email,Length,InputRequired
import email_validator



#CONTACT FORM
class ContactForm(FlaskForm):
    name = StringField("お名前 *",validators=[InputRequired(message='必須です')],render_kw={"placeholder": "例）ちっち　ヨーガ"})
    email = StringField('メールアドレス *',validators=[InputRequired(),Length(max=60), validators.Email(message='正しいメールアドレスを入力してください')],render_kw={"placeholder": "例）example@email.com"})
    subject = StringField('会社名',render_kw={"placeholder":"(任意)"})
    message = TextAreaField('お問合せ内容 *',validators=[InputRequired(message='お問あわせ内容を入力してください')],render_kw={"placeholder": "こちらにお問い合わせ内容を入力ください"})
    submit = SubmitField('送信する')
