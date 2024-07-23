from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db_url = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@db:5432/mydatabase')
    print(f"Connecting to database at: {db_url}")  # Debug print statement
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@db:5432/mydatabase')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
