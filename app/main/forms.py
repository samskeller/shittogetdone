from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, widgets
from wtforms.validators import Required


class MultipleCheckboxField(SelectField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class ShitToGetDoneForm(Form):
    to_do = MultipleCheckboxField('Shit')

    def __init__(self, shit, *args, **kwargs):
        shit_choices = [(x, x) for x in shit]
        self.to_do.kwargs['choices'] = shit_choices
        super(ShitToGetDoneForm, self).__init__(*args, **kwargs)

