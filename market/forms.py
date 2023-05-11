from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email,DataRequired,ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    #function for validation

    def validate_username (self, username_to_check):
        user = User.query.filter_by(username= username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! please try another username!')
    def validate_email_address(self, email_address_to_check):
        email_Address = User.query.filter_by (email_address= email_address_to_check.data).first()
        if email_Address:
            raise ValidationError('Email address alreeady exists please try another email address')


    username = StringField(label ='user name:', validators=[Length(min=2, max=30 ), DataRequired()])
    email_address = StringField(label ='email address:', validators=[Email(),DataRequired()])
    password1 = PasswordField(label = 'password:', validators=[Length(min = 6),DataRequired()])
    password2 = PasswordField(label = 'Confirm Password:', validators=[EqualTo('password1'),DataRequired()])
    submit  = SubmitField (label = 'Create Account')

class loginForm(FlaskForm):
    username = StringField(label= 'user name:', validators=[DataRequired()])
    password = PasswordField(label= 'password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in ')
  