import os
import requests

API_URL = "https://api.api-ninjas.com/v1/animals"


def load_env():
    """Lädt API_KEY aus der Datei .env (wenn vorhanden)."""
    if not os.path.exists(".env"):
        return

    with open(".env", "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'").strip('"')
            os.environ[key] = value


def fetch_data(animal_name):
    """Fetches animals data for the given animal_name from the API."""
    load_env()

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
