from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    
def register_blueprints(app):
    from src.routes.home import base_route
    from src.routes.auth import auth_route

    app.register_blueprint(base_route)
    app.register_blueprint(auth_route)