from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

rank = Blueprint('rank', __name__, url_prefix='/ranking')

@rank.route('/wargame', methods=['GET'])
def rank_wargame():
    return render_template('/web/rank_wargame.html')

@rank.route('/bugbounty', methods=['GET'])
def rank_bugbounty():
    return render_template('/web/rank_bugbounty.html')