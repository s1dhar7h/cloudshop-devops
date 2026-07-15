import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVICE_NAME = os.getenv("SERVICE_NAME", "notification-service")
    HOST = os.getenv("HOST","0.0.0.0")
    PORT = int(os.getenv("PORT",5004))
    DEBUG = os.getenv("DEBUG","True").lower() == "true"

    DB_HOST = os.getenv("DB_HOST", "postgres")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "cloudshop")
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")