# Add any model classes for Flask-SQLAlchemy here

from . import db
from datetime import datetime

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    poster = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)