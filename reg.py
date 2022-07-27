from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    firstName = StringField('First name',
                            validators=[DataRequired()])
    lastName = StringField('Last name',
                           validators=[DataRequired()])
    licensePlate = StringField('License plate number',
                               validators=[DataRequired()])
    cardNumber = StringField('Card number',
                             validators=[DataRequired(), Length(min=16, max=16)])
    expirationMonth = StringField('Expiration date (month)',
                             validators=[DataRequired(), Length(min=1, max=2)])
    expirationYear = StringField('Expiration date (year)',
                             validators=[DataRequired(), Length(min=1, max=2)])
    firstNameCard = StringField('First name',
                                validators=[DataRequired()])
    lastNameCard = StringField('Last name',
                               validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AdminLoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
