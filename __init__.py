from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow cross-origin requests for frontend-backend interaction
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from .routes import main  # Import routes
        app.register_blueprint(main)

        db.create_all()  # Create database tables

    return app
