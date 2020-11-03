from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import Config
from flask_restplus import Api

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    from flaskapp.api.concept import concept
    from flaskapp.api.statistics import statistics
    app.config.from_object(Config)

    db.init_app(app)


    api = Api(app)
    api.add_namespace(statistics)
    api.add_namespace(concept)

    return app
