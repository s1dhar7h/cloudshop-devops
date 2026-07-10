from utils.logger import logger
class UserService:

    @staticmethod
    def get_all_users():
        logger.info("Fetching all users")
        return [
            {
                "ID":1,
                "Name":"Sidharth",
                "email": "sid@example.com"
            },
            {
                "ID":2,
                "Name":"Muraleedharan",
                "email": "murli@example.com"
            }
        ]