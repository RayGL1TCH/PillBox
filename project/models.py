from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    device_id = db.Column(db.String(100))
    device_data =db.Column(db.String(1000))
    
#     medications = db.relationship('Medication', backref='user', lazy=True)


# class Medication(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     name = db.Column(db.String(100))
#     times = db.Column(db.JSON)  # Store medication times as JSON

#     def __repr__(self):
#         return f"Medication(name='{self.name}', times={self.times})"
