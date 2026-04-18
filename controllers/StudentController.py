from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.StudentService import StudentService

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['POST'])
@swag_from({
    'tags': ['Students'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'mother_last_name': {'type': 'string'},
                    'enrollment': {'type': 'string'},
                    'email': {'type': 'string'}
                },
                'required': ['first_name', 'last_name', 'mother_last_name', 'enrollment', 'email']
            }
        }
    ],
    'responses': {
        201: {'description': 'Student created successfully'},
        400: {'description': 'Invalid data'}
    }
})
def create_student():
    try:
        data = request.get_json()
        student = StudentService.create_student(
            data['first_name'],
            data['last_name'],
            data['mother_last_name'],
            data['enrollment'],
            data['email']
        )
        return jsonify(student.to_dict()), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@student_bp.route('/students', methods=['GET'])
@swag_from({
    'tags': ['Students'],
    'responses': {
        200: {'description': 'List of students'}
    }
})
def get_all_students():
    try:
        students = StudentService.get_all_students()
        return jsonify([student.to_dict() for student in students]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@student_bp.route('/students/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Students'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Student found'},
        404: {'description': 'Student not found'}
    }
})
def get_student_by_id(id):
    try:
        student = StudentService.get_student_by_id(id)
        return jsonify(student.to_dict()), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@student_bp.route('/students/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Students'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'},
                    'mother_last_name': {'type': 'string'},
                    'enrollment': {'type': 'string'},
                    'email': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Student updated'},
        404: {'description': 'Student not found'},
        400: {'description': 'Invalid data'}
    }
})
def update_student(id):
    try:
        data = request.get_json()
        student = StudentService.update_student(id, **data)
        return jsonify(student.to_dict()), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404 if 'not found' in str(e) else 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@student_bp.route('/students/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Students'],
    'parameters': [
        {'name': 'id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Student deleted'},
        404: {'description': 'Student not found'}
    }
})
def delete_student(id):
    try:
        StudentService.delete_student(id)
        return jsonify({'message': 'Student deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@student_bp.route('/students/date-range', methods=['GET'])
@swag_from({
    'tags': ['Students'],
    'parameters': [
        {
            'name': 'start_date',
            'in': 'query',
            'type': 'string',
            'format': 'date',
            'required': True,
            'description': 'Start date (YYYY-MM-DD)'
        },
        {
            'name': 'end_date',
            'in': 'query',
            'type': 'string',
            'format': 'date',
            'required': True,
            'description': 'End date (YYYY-MM-DD)'
        }
    ],
    'responses': {
        200: {'description': 'Students in date range'},
        400: {'description': 'Invalid parameters'}
    }
})
def get_students_by_date_range():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        
        if not start_date or not end_date:
            return jsonify({'message': 'start_date and end_date are required'}), 400
        
        students = StudentService.get_students_by_date_range(start_date, end_date)
        return jsonify([student.to_dict() for student in students]), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500