from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf import Form
from wtforms.validators import DataRequired, Email, Length


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')
