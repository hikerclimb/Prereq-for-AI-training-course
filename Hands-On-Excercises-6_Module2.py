import os
import json
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

with open("JsonApiUrl.json", "r") as f:
    config = json.load(f)

config["api_url"] = os.getenv("API_URL", "https://api.com")
print('working api:' + config['api_url'])
if not config['api_url']:
    print('api_url is empty')
