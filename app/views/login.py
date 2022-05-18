from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

login = Blueprint('login', __name__, url_prefix='/')

@login.route('/login', methods=['GET'])
def index():
    return render_template('/web/login.html')
