from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email, Regexp


class NameForm(Form):
    name = StringField('Your Name', validators=[Required()])
    submit = SubmitField('Submit')

class DeleteForm(Form):
    delete = SubmitField('Delete')