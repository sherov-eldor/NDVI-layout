from flask import flash, render_template, redirect, url_for, Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from src.forms.login import LoginForm
from src.models.user import User
from src.utils.extensions import db
from flask_login import login_user, logout_user


auth_route = Blueprint('auth_route', __name__, url_prefix='/auth')


@auth_route.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_query = User.query.filter_by(username=form.data['username']).first()
        if user_query:
            checked_password = check_password_hash(user_query.password, form.data['password'])
            if checked_password:
                # flash(f"{user_query.username}", 'success')
                login_user(user_query, remember=form.data['remember'])
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('base_route.home'))
            else:
                # flash(f"Parol xato!!!", 'danger')
                return redirect(url_for('auth_route.login'))
        else:
            hashed_password = generate_password_hash(form.data['password'])
            user = User(username=form.data['username'], password=hashed_password)
            login_user(user, remember=form.data['remember'])
            db.session.add(user)
            db.session.commit()
            # flash(f"{user.username}", 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('base_route.home'))
    return render_template('auth/login.html', title='Login', form=form)


@auth_route.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_route.login'))