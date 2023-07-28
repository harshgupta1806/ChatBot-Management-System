from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import Length, DataRequired, equal_to, ValidationError

from dashboard.models import Login
from database.local_settings import alert_code


class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=5, max=30), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    remember_me = BooleanField(label='Keep me signed in')
    submit = SubmitField(label='Sign-In')


class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=5, max=30), DataRequired()])
    first_name = StringField(label='First Name', validators=[Length(min=5), DataRequired()])
    last_name = StringField(label='Last Name', validators=[Length(min=5), DataRequired()])
    image_url = StringField(label='Image-URL')
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[Length(min=8), DataRequired(), equal_to('password')])
    designation = SelectField(default='Designation',
                              choices=[('developer', 'Developer'), ('admin', 'Admin'), ('faculty', 'Faculty')],
                              validators=[DataRequired()])
    submit = SubmitField(label='Sign-Up')

    def validate_username(self, username_to_check):
        """check if username already exist in database
        params:
            username_to_check (form object): username to check
        """
        username = Login.query.filter_by(username=username_to_check.data).first()
        if username is not None:
            raise ValidationError('Username is already taken! Please try different username!! ')


class AlertForm(FlaskForm):
    choices_key = list(alert_code.keys())

    choices = []
    for key in choices_key:
        if key == 'college':
            choices.append((alert_code[key], 'All Users'))
        else:
            choices.append((alert_code[key], f'{key.title()} Engg. Students'))

    alert_message = TextAreaField(label='Alert Message', validators=[Length(min=5), DataRequired()])
    send_to = SelectField(default='Send Alert To',
                          choices=choices,
                          validators=[DataRequired()])
    submit = SubmitField(label='Send Alert')


