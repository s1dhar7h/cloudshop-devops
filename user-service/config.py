import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVICE_NAME = "user-service"
    HOST = os.getenv("HOST","0.0.0.0")
    PORT = int(os.getenv("PORT",5001))
    DEBUG = os.getenv("DEBUG","True").lower() == "true"