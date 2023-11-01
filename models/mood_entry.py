from flask_sqlalchemy import SQLAlchemy
from config import db, app, login_manager
from datetime import datetime
from models.user import User


class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood_type = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.String(200))
    entry_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='mood_entries')

    def __init__(self, mood_type, notes, user_id=User.id):
        self.mood_type = mood_type
        self.notes = notes
        self.user_id = user_id

    def __str__(self):
        return f"{self.mood_type} entry on {self.entry_date}"