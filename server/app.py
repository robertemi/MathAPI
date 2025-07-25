from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config, get_db_connection, return_db_connection, get_redis_client
from controllers.MathController import MathController
from schemas import FactorialRequest, PowerRequest, FibbonaciRequest
from pydantic import ValidationError
from werkzeug.security import check_password_hash
from models.User import User
from controllers.UserController import UserController


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    redis_client = get_redis_client()

    CORS(app,
         resources={r"/*": {"origins": "*"}},
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
         allow_headers=['Content-Type', 'Authorization', 'Accept',
                        'Origin', 'X-Requested-With'],
         supports_credentials=False)
    

    @app.route(rule='/auth', methods=['POST'])
    def auth_user():
        db_connection = get_db_connection()
        controller = UserController()
        try:
            data = request.get_json()

            if not data or 'email' not in data or 'password' not in data:
                return jsonify({"error": "Email and password required"}), 400

            email = data['email']
            password = data['password']

            user_exists = controller.handle_user_auth(
                db_connection,
                email,
                password
            )

            if user_exists:
                return jsonify({"message": "User authentication successfull"}), 201
            else:
                return jsonify({"error": "User could not be authenticated"}), 500

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            return_db_connection(db_connection)


    @app.route(rule='/sign-up', methods=['POST'])
    def sign_up_user():
        db_connection = get_db_connection()
        controller = UserController()
        try:
            data = request.get_json()

            if not data or 'first_name' not in data or 'last_name' not in data or 'email' not in data or 'password' not in data:
                return jsonify({"error": "Missing required fields"}), 400
            
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            password = data['password']
            role = data.get('role')

            success = controller.handle_user_sign_up(
                db_connection, 
                first_name,
                last_name,
                email,
                password,
                role
            )

            if success:
                return jsonify({"message": "User created successfully"}), 201
            else:
                return jsonify({"error": "User could not be created"}), 500
            
        except Exception as e:
            print(f'Exception in user creation app.py: {e}')
        
        finally:
            return_db_connection(db_connection)

    @app.route(rule='/compute/<operation>', methods=['POST'])
    def compute(operation):
        db_connection = get_db_connection()
        controller = MathController(redis_client)

        try:
            data = request.get_json()

            if operation == "factorial":
                validated = FactorialRequest(**data).model_dump()
            elif operation == "power":
                validated = PowerRequest(**data).model_dump()
            elif operation == "fibbonaci":
                validated = FibbonaciRequest(**data).model_dump()
            else:
                return jsonify({"error": f"Unsupported operation: {operation}"}), 400
            
            result = controller.handle_request(
                db_connection,
                operation,
                **validated
            )
            return jsonify({"result": result}), 200

        except ValidationError as ve:
            return jsonify({"error": ve.errors()}), 422
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": "Internal server error"}), 500
        finally:
            return_db_connection(db_connection)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host=app.config.get('HOST', '0.0.0.0'),
        port=app.config.get('PORT', 5000),
        debug=app.config.get('DEBUG', False)
    )
