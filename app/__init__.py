from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(Config)

    login.login_view='/login'
    login.login_message="Make sure you log in"

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.blueprints.social import bp as social_bp
    app.register_blueprint(social_bp)
    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app

from app.blueprints.social import models