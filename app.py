from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this to a secure secret key
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'  # Replace with your database connection details

#db = SQLAlchemy(app)

# Define the User model for the database
""" class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) """

# Routes for your web app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        # You can add user authentication and session management here
        return redirect(url_for('index'))"""
    return render_template('sign_up.html')

@app.route('/home' , methods=[ 'GET', 'POST'])
def home():
   return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    """if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement user authentication here
        # If login is successful, set user session
        return redirect(url_for('index'))"""
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
