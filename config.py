import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")  # load API_KEY from local .env
