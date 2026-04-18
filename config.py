import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.environ.get('FLASK_ENV', 'development')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:131023@localhost:3307/students')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta_123')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'mi_jwt_secreta_456')