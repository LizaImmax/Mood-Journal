from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, logout_user, current_user
from basemodel import RegistrationForm, Mood_JournalForm, LoginForm
from config import app, db, bcrypt, login_manager  
from models.mood_entry import MoodEntry
from models.journal_entry import JournalEntry
from models.user import User

def get_current_user():
    return current_user

# Routes for your web app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Register', form=form)


@app.route('/home' , methods=[ 'GET', 'POST'])
def home():
   form = Mood_JournalForm()
   if form.validate_on_submit():
        return redirect(url_for('login'))
   return render_template('home.html' , form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        app.logger.info(f"User: {user}")
        app.logger.info(f"Form Email: {form.email.data}")
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            app.logger.info("Password check: Success")
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('account'))  # Redirect to the user's account page
        else:
            app.logger.info("Password check: Failed")
            flash('Login unsuccessful. Please check your email and password.', 'error')
    return render_template('login.html', title='Login', form=form)

@app.route('/privacy', methods=['GET', 'POST'])
def privacy():
    return render_template('privacy.html')

@app.route('/terms', methods=['GET', 'POST'])
def terms():
    return render_template('terms.html')

@app.route('/save_mood_journal', methods=['POST'])
def save_mood_journal():
    if request.method == 'POST':
        return redirect(url_for('home'))
    
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Logs the user out
    return redirect(url_for('login'))  # Redirect to the login page or any other desired page

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')


if __name__ == '__main__':
    app.run(debug=True)
