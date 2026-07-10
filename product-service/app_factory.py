from flask import Flask ,jsonify
from routes.product_routes import product_bp
from utils.response import error_response

def create_app():
    app=Flask(__name__)

    app.register_blueprint(product_bp)

    @app.errorhandler(404)

    def not_found(error):
        return error_response(
            "Resource not found",
            404
        )
    return app