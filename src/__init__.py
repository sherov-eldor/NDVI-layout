from flask import Flask
from src.utils.extensions import register_blueprints, register_extensions


def create_app(config:str):
    app = Flask(__name__)

    if config in ['dev', 'prod', 'test']:
        app.config.from_object(f"src.config.config.{config.capitalize()}Config")

    register_extensions(app)
    register_blueprints(app)

    with app.app_context():
        from src.utils.extensions import db
        from src.models.user import User

        db.create_all()
        # db.drop_all()
        
    return app