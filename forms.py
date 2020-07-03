from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    searchphrase = StringField('SearchPhrase',
                        validators=[DataRequired()])
    submit = SubmitField('Fetch!')
