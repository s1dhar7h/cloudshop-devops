from flask import Blueprint,jsonify
from services.user_services import UserService
from utils.response import success_response

#user_bp = Blueprint("user",__name__)

user_bp = Blueprint("user",
                    __name__,
                    url_prefix="/api/v1"
)

@user_bp.route("/")
def home():
    return success_response({
        "service": "user-service",
        "status": "running"
    })

@user_bp.route("/health")
def health():
    return success_response({
        "status": "healthy"
    })

@user_bp.route("/users")
def users():
    return success_response(
        UserService.get_all_users()
    )
    # return jsonify({
    #     "users": [
    #         {
    #             "ID":1,
    #             "Name":"Sidharth",
    #             "email": "sid@example.com"
    #         },
    #         {
    #             "ID":2,
    #             "Name":"Muraleedharan",
    #             "email": "murli@example.com"
    #         }
    #     ]
    # })