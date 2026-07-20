from database.db import get_connection
from utils.logger import logger


class UserService:

    @staticmethod
    def get_all_users():

        logger.info("Fetching all users from PostgreSQL")

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, email FROM users"
        )

        rows = cursor.fetchall()

        cursor.close()

        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }
            for row in rows
        ]