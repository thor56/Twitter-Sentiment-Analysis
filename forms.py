from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    searchphrase = StringField('SearchPhrase', [DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Fetch')
