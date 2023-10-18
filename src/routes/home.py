from flask import render_template, Blueprint, redirect, url_for, request, jsonify
from flask_login import login_required
from src.forms.upload import UploadForm
import os
from werkzeug.utils import secure_filename

base_route = Blueprint('base_route', __name__, url_prefix='/')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@base_route.route('/',methods=['GET', 'POST'])
@login_required
def home():
    form = UploadForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        return jsonify('ok')
    else:
        print('error: ', form.errors)
    return render_template('index.html', form=form)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS