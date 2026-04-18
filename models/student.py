from extension import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    mother_last_name = db.Column(db.String(100), nullable=False)
    enrollment = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'mother_last_name': self.mother_last_name,
            'enrollment': self.enrollment,
            'email': self.email,
            'registration_date': self.registration_date.strftime('%Y-%m-%d %H:%M:%S') if self.registration_date else None
        }