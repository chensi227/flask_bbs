# -*- coding: utf-8 -*-
from flask import Blueprint
mod = Blueprint('auth', __name__)

from . import views
