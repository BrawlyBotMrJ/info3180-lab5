# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Movie Poster', validators=[InputRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])