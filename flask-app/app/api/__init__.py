# -*- coding: utf-8 -*-
from flask import Blueprint
mod = Blueprint('api', __name__)

from . import authentication, errors

