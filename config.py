import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://myuser:mypassword@db:5432/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
