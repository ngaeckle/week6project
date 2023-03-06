from . import bp as auth_bp
from app.forms import RegisterForm, SignInForm
from app.blueprints.social.models import User
from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, login_required


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        u = User(username=username,email=email,password_hash='')
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username: {username} already exists, try again')
            return redirect('/register')
        elif email_match:
            flash(f'Email: {email} already exists, try again')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Login for {username} successful')
            return redirect('/')

    return render_template('register.jinja',title='Register', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match:
            flash(f'Username or Password was incorrect, try again')
            return redirect('/login')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.jinja',title='Login', form=form)

@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')
