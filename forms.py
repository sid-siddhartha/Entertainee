from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators, RadioField, EmailField
from wtforms.validators import InputRequired


class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegistrationForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = EmailField('E-Mail', validators=[InputRequired()])
    phoneno = StringField('Phone No', validators=[InputRequired()])
    address = StringField('Address')
    submit = SubmitField('SignUp')
