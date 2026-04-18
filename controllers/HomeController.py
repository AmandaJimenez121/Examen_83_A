from flask import Blueprint, jsonify

Blueprint_home = Blueprint('home', __name__)

@Blueprint_home.route('/home')
def home():
    return jsonify({'message': 'API funcionando correctamente'}), 200