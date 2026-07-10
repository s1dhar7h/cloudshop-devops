#from flask import Flask ,jsonify
from config import Config
#from routes.user_routes import user_bp
from app_factory import create_app

#app=Flask(__name__)

# @app.route("/")
# def home():
#     return jsonify({
#         "Service":"User Service",
#         "Status":"Running"
#     })

# @app.route("/health")
# def health():
#     return jsonify({
#         "Status":"Healthy"
#     })

# @app.route("/users")
# def users():
#     return jsonify({
#         "users": [
#             {
#                 "ID":1,
#                 "Name":"Sidharth"
#             },
#             {
#                 "ID":2,
#                 "Name":"Muraleedharan"
#             }
#         ]
#     })


#app.register_blueprint(user_bp)

# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({
#         "error" : "Resource not found"
#     }) , 404

app=create_app()

if __name__ == "__main__":
    app.run(
        host = Config.HOST,
        port = Config.PORT,
        debug = Config.DEBUG
    )
    #    app.run(host="0.0.0.0",port=5001)