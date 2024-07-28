from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db_url = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@db:5432/mydatabase')
    app.logger.info(f"Connecting to database at: {db_url}")  # Improved logging

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Ensure models are imported
        from .models import User
        from . import routes

        # Create tables
        db.create_all()

    return app
