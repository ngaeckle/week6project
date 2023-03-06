from . import bp as main_bp
from flask import render_template
from flask import redirect, render_template, url_for
from flask_login import login_required, current_user
from app.forms import PokemonCatchForm
from flask import render_template, redirect, flash
from app.blueprints.social.models import Pokemon, User
import requests, random

num = random.randint(0, 100)

@main_bp.route('/', methods=['GET','POST'])
def index():
    #return redirect('/login')
    return render_template('index.jinja', title='Home')

@main_bp.route('/catch', methods=['GET','POST'])
@login_required
def catch():
    form = PokemonCatchForm()
    url = f'https://pokeapi.co/api/v2/pokemon/{num}'
    response = requests.get(url)
    data = response.json()
    if form.validate_on_submit():
        flash('Validated')
        name=data['name']
        description=f'{name} is really cool, and super good'
        type=data['types'][0]['type']['name']
        p = Pokemon(name=name, description=description,type=type, user_id=current_user.id)
        p.commit()
        flash('Commited pokemon')
        return redirect(url_for("social.user", username=current_user.username))
    return render_template('catch.jinja', title='Home', data=data, form=form)


