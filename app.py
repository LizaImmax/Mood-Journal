from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, logout_user, current_user
from basemodel import RegistrationForm, Mood_JournalForm
from config import app, db, bcrypt
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
        hushed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        with app.app_context():
            user = User(username=form.username.data, email=form.email.data, password=hushed_password)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('login'))
    return render_template('sign_up.html', form=form, title="Register")

@app.route('/home' , methods=[ 'GET', 'POST'])
def home():
   form = Mood_JournalForm()
   if form.validate_on_submit():
        return redirect(url_for('login'))
   return render_template('home.html' , form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

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


if __name__ == '__main__':
    app.run(debug=True)
