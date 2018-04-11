# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from app import db
from app.models import User
from flask import flash
from flask_login import login_user, login_required, logout_user
from . forms import LoginForm

from flask_cors import CORS


from . import mod

CORS(mod)

from flask_socketio import SocketIO, emit, send


__author__ = '陈偲'

@mod.route('/')
def index():
    return 'auth index'


@mod.route('/login/')
def hello():
    # resp = jsonify({'error': False})
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    return jsonify({'token': 'chensi', 'duration': 600})


