from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

select_choices = ["Yes", "No", "I don't know"]


class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Address', validators=[DataRequired()])
    maps_url = StringField('Cafe Location on Google Maps (URL)', validators=[URL(message="Please provide a URL")])
    open = TimeField('Opening Time')
    close = TimeField('Closing Time')
    wifi = SelectField('Wifi available?', choices=select_choices, default="I don't know")
    sockets = SelectField('Power Sockets available?', choices=select_choices, default="I don't know")
    mountain_views = SelectField('Mountain Views?', choices=select_choices, default="I don't know")
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    review_text = CKEditorField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit Review")


class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In!")


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email(message="Please provide a valid Email Address")])
    phone = StringField("Phone Number")
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Email")