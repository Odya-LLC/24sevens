from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.configs.config.Config")
    db.init_app(app)
    from app.api import api_bp
    app.register_blueprint(api_bp)
    with app.app_context():
        db.create_all()
    return app