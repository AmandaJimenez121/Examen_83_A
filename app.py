from flask import Flask
from controllers.HomeController import Blueprint_home
from extension import db, migrate, swagger, jwt
from config import Config
from controllers.AuthController import auth_bp
from controllers.StudentController import student_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app) 
    jwt.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(student_bp, url_prefix='/api')
    app.register_blueprint(Blueprint_home)

    @app.route('/')
    def home():
        return {'message': 'Students API is running'}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)