from database.db import get_connection
from utils.logger import logger


class NotificationService:

    @staticmethod
    def get_all_notifications():

        logger.info("Fetching all notifications from PostgreSQL")

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, user_id, message
            FROM notifications
            """
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            {
                "id": row[0],
                "user_id": row[1],
                "message": row[2]
            }
            for row in rows
        ]