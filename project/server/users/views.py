# project/server/users/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

auth_blueprint = Blueprint('index', __name__)

class UsersAPI(MethodView):
    """
    User Index Resource
    """
    def get(self):
        user = User.query.order_by(User.email).all()
        return make_response(jsonify(user)), 201
# define the API resources
users_view = UsersAPI.as_view('users_api')

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)
