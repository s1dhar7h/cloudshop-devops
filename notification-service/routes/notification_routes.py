from flask import Blueprint,jsonify
from services.notification_services import NotificationService
from utils.response import success_response

#user_bp = Blueprint("user",__name__)

notification_bp = Blueprint("notification",
                    __name__,
                    url_prefix="/api/v1"
)

@notification_bp.route("/")
def home():
    return success_response({
        "service": "notification-service",
        "status": "running"
    })

@notification_bp.route("/health")
def health():
    return success_response({
        "status": "healthy"
    })

@notification_bp.route("/notifications")
def notifications():
    return success_response(
        NotificationService.get_all_notifications()
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