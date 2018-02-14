from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	submit = SubmitField('Sign In')