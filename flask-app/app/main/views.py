# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect, url_for
from app import db
from app.models import User
from flask import flash
from flask_login import login_user, login_required, logout_user
from . import mod
from flask import current_app


__author__ = '陈偲'

@mod.route('/')
def index():
    return current_app.config['SECRET_KEY']