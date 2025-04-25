import os
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = os.getenv("API_BASE_URL")

if not BASE_API_URL:
    raise ValueError("API_BASE_URL environment variable is not set.")
