from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config, get_db_connection, return_db_connection, get_redis_client
from controllers.MathController import MathController
from schemas import FactorialRequest, PowerRequest, FibbonaciRequest
from pydantic import ValidationError


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

    @app.route(rule='/compute/<operation>', methods=['POST'])
    def compute(operation):
        db_connection = get_db_connection()
        controller = MathController(db_connection, redis_client)

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
