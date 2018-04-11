# -*- coding: utf-8 -*-
from flask import Blueprint

mod = Blueprint('main', __name__)

from . import views



