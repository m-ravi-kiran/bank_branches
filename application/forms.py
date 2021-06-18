from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    radio_button = RadioField("", choices=[('Search by IFSC', 'Search by IFSC'), ('Search by name', 'Search by name')])


class SearchByIFSCForm(FlaskForm):
    ifsc_code = StringField('IFSC Code', validators=[DataRequired(), Length(min=11, max=11)])
    submit = SubmitField('OK')


class SearchByNameForm(FlaskForm):
    pass
