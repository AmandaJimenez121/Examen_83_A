from services.AuthService import AuthService
from flask import Blueprint, request, jsonify
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ['User'],
    'parameters': [
        {'name': 'body', 
        'in': 'body',
        'schema': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'email': {'type': 'string'},
                'password': {'type': 'string'}
            },
            'required': ['username', 'email', 'password']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuario creado',
        }
    }
})
def register():
    data = request.get_json()
    try:
        user = AuthService.register(data['username'], data['email'], data['password'])
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Auth'],
    'parameters': [
        {'name': 'body', 
        'in': 'body',
        'schema': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'password': {'type': 'string'}
            },
            'required': ['username', 'password']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Login successful',
        }
    }
})
def login():
    data = request.get_json()
    result = AuthService.login(data['username'], data['password'])
    if not result:
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = result['access_token']
    user = result['user']
    return jsonify({
        "access_token": access_token,
        'user': user.to_dict()
    }), 200