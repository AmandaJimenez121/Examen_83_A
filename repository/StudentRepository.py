from models.student import Student
from extension import db
from datetime import datetime

class StudentRepository:
    @staticmethod
    def create(first_name, last_name, mother_last_name, enrollment, email):
        student = Student(
            first_name=first_name,
            last_name=last_name,
            mother_last_name=mother_last_name,
            enrollment=enrollment,
            email=email
        )
        db.session.add(student)
        db.session.commit()
        return student
    
    @staticmethod
    def get_all():
        return Student.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Student.query.get(id)
    
    @staticmethod
    def get_by_enrollment(enrollment):
        return Student.query.filter_by(enrollment=enrollment).first()
    
    @staticmethod
    def get_by_email(email):
        return Student.query.filter_by(email=email).first()
    
    @staticmethod
    def update(id, **kwargs):
        student = Student.query.get(id)
        if student:
            for key, value in kwargs.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            db.session.commit()
        return student
    
    @staticmethod
    def delete(id):
        student = Student.query.get(id)
        if student:
            db.session.delete(student)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_by_date_range(start_date, end_date):
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        end_date_dt = end_date_dt.replace(hour=23, minute=59, second=59)
        
        return Student.query.filter(
            Student.registration_date >= start_date_dt,
            Student.registration_date <= end_date_dt
        ).all()