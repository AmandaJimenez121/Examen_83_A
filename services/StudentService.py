from repository.StudentRepository import StudentRepository

class StudentService:
    @staticmethod
    def create_student(first_name, last_name, mother_last_name, enrollment, email):
        if StudentRepository.get_by_enrollment(enrollment):
            raise ValueError('Enrollment already exists')
        
        if StudentRepository.get_by_email(email):
            raise ValueError('Email already exists')
        
        student = StudentRepository.create(
            first_name, last_name, mother_last_name, 
            enrollment, email
        )
        return student
    
    @staticmethod
    def get_all_students():
        return StudentRepository.get_all()
    
    @staticmethod
    def get_student_by_id(id):
        student = StudentRepository.get_by_id(id)
        if not student:
            raise ValueError('Student not found')
        return student
    
    @staticmethod
    def update_student(id, **data):
        student = StudentRepository.get_by_id(id)
        if not student:
            raise ValueError('Student not found')
        
        if 'enrollment' in data and data['enrollment'] != student.enrollment:
            if StudentRepository.get_by_enrollment(data['enrollment']):
                raise ValueError('Enrollment already exists')
        
        if 'email' in data and data['email'] != student.email:
            if StudentRepository.get_by_email(data['email']):
                raise ValueError('Email already exists')
        
        student = StudentRepository.update(id, **data)
        return student
    
    @staticmethod
    def delete_student(id):
        student = StudentRepository.get_by_id(id)
        if not student:
            raise ValueError('Student not found')
        
        return StudentRepository.delete(id)
    
    @staticmethod
    def get_students_by_date_range(start_date, end_date):
        return StudentRepository.get_by_date_range(start_date, end_date)