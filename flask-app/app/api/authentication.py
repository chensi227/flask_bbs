# -*- coding: utf-8 -*-
from flask import g, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from ..models import User
from . import mod
from .errors import unauthorized, forbidden
from flask_cors import CORS

auth = HTTPBasicAuth()

CORS(mod)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    g.current_user = User.verify_auth_token(username_or_token)
    return True




@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@mod.route('/resource/')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})

@mod.route('/token/')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@mod.route("/")
@auth.login_required
def index():
    return jsonify('Hello, %s' % g.user.username)




@mod.route('/login/')
def hello():
    return jsonify({'token': 'chensi', 'duration': 600})