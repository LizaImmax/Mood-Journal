from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'