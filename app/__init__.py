from flask import Flask 

from app.extensions import db, migrate
from app.routes.main import main
from app.routes.api import api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app