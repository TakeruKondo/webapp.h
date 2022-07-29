from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from flaskblog.models import User


class RegistrationForm(FlaskForm):
 
    email = StringField('メールアドレス',
                        validators=[DataRequired(), Email(message='正しいメールアドレスを入力してください')],render_kw={"placeholder": "例）example@email.com"})
    password = PasswordField('パスワード', validators=[DataRequired(),Length(min=3,max=20,message='3文字以上20文字以内で入力')],render_kw={"placeholder": "パスワードを入力..."})
    confirm_password = PasswordField('パスワード（確認用）',
                                     validators=[DataRequired(), EqualTo('password',message="パスワードが一致しません")],render_kw={"placeholder": "パスワード (確認用)を入力..."})
    submit = SubmitField('Sign Up')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is taken. Please choose a different one.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('メールアドレス',
                        validators=[DataRequired(), Email(message='正しいメールアドレスを入力してください')],render_kw={"placeholder": "例）example@email.com"})
    password = PasswordField('パスワード', validators=[DataRequired()],render_kw={"placeholder": "パスワードを入力..."})
    remember = BooleanField('ログイン情報を保存する')
    submit = SubmitField('ログイン')



class RequestResetForm(FlaskForm):
    email = StringField('メールアドレス',
                        validators=[DataRequired(), Email(message='正しいメールアドレスを入力してください')],render_kw={"placeholder":"例）example@email.com"})
    submit = SubmitField('パスワードをリセット')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is None:
    #         raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('パスワード', validators=[DataRequired()])
    confirm_password = PasswordField('パスワード（確認用',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('パスワードをリセット')