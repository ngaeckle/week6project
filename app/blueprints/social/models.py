from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import requests


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    characters = db.relationship('Pokemon', backref='my_pokemon', lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def __str__(self) -> str:
        return f'<User: {self.email}|{self.username}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(140))
    type = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def get_data(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.name}'
        response = requests.get(url)
        return response.json()