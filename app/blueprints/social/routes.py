from . import bp as social_bp
from flask import redirect, render_template, url_for
from .models import User
from flask_login import login_required, current_user
from flask import render_template, redirect, flash
import requests
from app.blueprints.social.models import Pokemon, User


@social_bp.route('/user/<username>', methods=['GET','POST'])
@login_required
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/login')
    '''url = 'https://pokeapi.co/api/v2/pokemon/squirtle'
    response = requests.get(url)
    data = response.json()    
    name=data['name']
    description=f'{name} is really cool, and super good'
    type=data['types'][0]['type']['name']
    p = Pokemon(name=name, description=description,type=type, user_id=current_user.id)
    p.commit()'''
    pokedex = user_match.characters
    return render_template('user.jinja', user=user_match, pokedex=pokedex)
