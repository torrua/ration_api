import os

from dotenv import load_dotenv

load_dotenv()

SECRET_TOKEN_RESET_PASSWORD = os.getenv("SECRET_TOKEN_RESET_PASSWORD")
SECRET_TOKEN_VERIFICATION = os.getenv("SECRET_TOKEN_VERIFICATION")
JWT_SECRET = os.getenv("SECRET_JWT")
SQL_REQUESTS_ECHO = bool(int(os.environ.get("SQL_REQUESTS_ECHO", 0)))
APP_NAME = os.getenv("APP_NAME", "UNKNOWN")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_RULE = os.getenv("DB_RULE", "")
