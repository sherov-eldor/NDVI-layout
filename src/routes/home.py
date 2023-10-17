from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required

base_route = Blueprint('base_route', __name__, url_prefix='/')

@base_route.route('/')
@login_required
def home():
    # return redirect(url_for('auth_route.login'))
    return render_template('index.html')