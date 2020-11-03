from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import Config
from flask_restplus import Api

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    from flaskapp.api.person import person
    from flaskapp.api.main import main
    app.config.from_object(Config)

    db.init_app(app)


    api = Api(app)
    api.add_namespace(main)

    return app
