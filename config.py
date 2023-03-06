import os

class Config():
    SECRET_KEY='bruhliterallyanything'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')