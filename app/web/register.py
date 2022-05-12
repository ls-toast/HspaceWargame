from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

register = Blueprint('register', __name__, url_prefix='/')

@register.route('/register', methods=['GET'])
def index():
    return render_template('/web/register.html')
