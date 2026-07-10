from utils.logger import logger
class NotificationService:

    @staticmethod
    def get_all_notifications():
        logger.info("Fetching all notifications")
        return [
            {
                "id": 1,
                "type": "Email",
                "message": "Order shipped"
            }
        ]