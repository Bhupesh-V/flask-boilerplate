from flask import Blueprint

from app.extensions import db
from app.models.user import User

main = Blueprint('main', __name__)

@main.route('/user/<name>')
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    return f'Created User {name}!'