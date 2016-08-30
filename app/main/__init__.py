import sys
sys.path.append('/usr/lib/python2.7/site-packages')
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
