from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from flask_smorest import Api
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def app_factory(configurations):
    app = Flask(__name__)

    app.config.from_object(config[configurations])

    db.init_app(app)
    jwt.init_app(app)

    Migrate(app=app, db=db)
#   Blueprint imports
    from app.auth import blp as auth_blp
    from app.pharmacy import blp as pharmacy_blp
#   Register SmoRest API and Blueprints

    api = Api(app)
    api.register_blueprint(auth_blp)
    api.register_blueprint(pharmacy_blp)
    

    

    
    return app