from flask import Blueprint

from ..extensions import db
from ..models.user import User

api = Blueprint('api', __name__)

@api.route('/user/<name>')
def get_user(name):
    user = User.query.filter_by(name=name).first()

    return {'user': user.name}