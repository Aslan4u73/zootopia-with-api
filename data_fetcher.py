import os
import requests
from dotenv import load_dotenv

API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """Fetches animals data for the given animal_name from the API."""
    load_dotenv()

    api_key = os.getenv("API_KEY")
    if not api_key:
        print("ERROR: API_KEY fehlt! Bitte in .env setzen: API_KEY='...'")
        return []

    response = requests.get(
        API_URL,
        headers={"X-Api-Key": api_key},
        params={"name": animal_name},
    )

    if response.status_code != 200:
        print("ERROR:", response.status_code, response.text)
        return []

    return response.json()
