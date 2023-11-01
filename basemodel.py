from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, ValidationError, DataRequired, Email, EqualTo
from models.user import User

class RegistrationForm(FlaskForm):
    """ Registration method to allow user creat an account.
    Validates if the account meets the requirements, and creates the account

    Args:
        FlaskForm (_type_): _Flask Object to process user login_

    Raises:
        ValidationError: _Raises a validation error when the user registers
        with an email existing in the db_
    """
    username = StringField('Username', validators=[DataRequired()],
                        render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "email"})
    
    password = PasswordField('Password', validators=[DataRequired(),
                                         Length(min=6, max=20)],
                                    render_kw={"placeholder": "password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],
                                    render_kw={"placeholder": "confirm password"})
    submit = SubmitField("Register")

    def validate_email(self, email):
        """validate user account creation by checking if email exists already

        Args:
            email (_type_): _parameter to check_

        Raises:
            ValidationError: _The error to raise if email exists_
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email address is registered, log in or register with another email')
        


class Mood_JournalForm(FlaskForm):
    """ Registration method to allow user creat an account.
    Validates if the account meets the requirements, and creates the account

    Args:
        FlaskForm (_type_): _Flask Object to process user login_

    Raises:
        ValidationError: _Raises a validation error when the user registers
        with an email existing in the db_
    """
    mood = StringField('Mood', validators=[DataRequired()],
                        render_kw={"placeholder": "mood"}) 
    journal = StringField('Journal', validators=[DataRequired()],
                        render_kw={"placeholder": "journal"}) 
    submit = SubmitField("Save")


