from flask_wtf import Form
from wtforms import StringField , BooleanField , PasswordField , SubmitField,ValidationError
from wtforms.validators import DataRequired,Required,Length,Email,EqualTo,Regexp


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])