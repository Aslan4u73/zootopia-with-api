import os
import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY_ENV = "API_NINJAS_KEY"


def fetch_data(animal_name):
    """Fetches animals data for the given animal_name from the API."""
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        print("ERROR: API Key fehlt! Terminal: export API_NINJAS_KEY='...'")
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
