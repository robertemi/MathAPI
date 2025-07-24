from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config, get_db_connection, return_db_connection
from controllers.MathController import MathController


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    CORS(app,
         resources={r"/*": {"origins": "*"}},
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
         allow_headers=['Content-Type', 'Authorization', 'Accept',
                        'Origin', 'X-Requested-With'],
         supports_credentials=False)

    @app.route(rule='/compute/<operation>', methods=['POST'])
    def compute(operation):
        db_connection = get_db_connection()

        try:
            controller = MathController(db_connection)
            result = controller.handle_request(
                operation,
                **request.get_json()
            )
            return jsonify({"result": result}), 200
            
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
            
        except Exception as e:
            return jsonify({"error": "Internal server error app"}), 500   

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
