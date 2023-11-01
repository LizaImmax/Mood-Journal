from flask_sqlalchemy import SQLAlchemy
from config import db, app, login_manager
from datetime import datetime
from models.user import User


class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    entry_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='journal_entries')

    def __init__(self, content, user_id=User.id):
        self.content = content
        self.user_id = user_id

    def __str__(self):
        return f"Journal entry on {self.entry_date}"