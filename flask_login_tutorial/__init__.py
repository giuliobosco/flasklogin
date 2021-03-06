"""Initialize app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    
    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # create database models
        db.create_all()

        # compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

    return app
