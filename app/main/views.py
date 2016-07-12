from flask import render_template, session, redirect, url_for
from . import main
from .forms import ShitToGetDoneForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    to_get_done = session.get('to_get_done', ['Laundry', 'Dishes'])
    form = ShitToGetDoneForm(to_get_done)
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    session['to_get_done'] = ['Wallpaper', 'Cat Litter']
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))
