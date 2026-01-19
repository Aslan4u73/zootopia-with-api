import os
import requests


def load_data_from_api(name):
    """Holt Tiere von der API und gibt eine Liste zurück."""
    api_key = os.getenv("API_NINJAS_KEY")
    if not api_key:
        print("ERROR: API Key fehlt! Terminal: export API_NINJAS_KEY='...'")
        return []

    url = f"https://api.api-ninjas.com/v1/animals?name={name}"
    response = requests.get(url, headers={"X-Api-Key": api_key})

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("ERROR:", response.status_code, response.text)
        return []

    return response.json()


def serialize_animal(animal):
    """Macht aus einem Tier-Dict ein kleines HTML-Stück."""
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    locations = animal.get("locations", [])
    location = locations[0] if locations else "Unknown"
    animal_type = animal.get("characteristics", {}).get("type")

    html = f'<div class="card__title">{name}</div><br/>'
    html += '<p class="card__text">'
    html += f"Diet: {diet}<br/>"
    html += f"Location: {location}<br/>"
    if animal_type:
        html += f"Type: {animal_type}<br/>"
    return html


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = load_data_from_api(animal_name)

    if not animals_data:
        output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        output = '<ul class="cards">'
        for animal in animals_data:
            output += '<li class="cards__item">'
            output += serialize_animal(animal)
            output += "</p></li>"
        output += "</ul>"

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(template.replace("__REPLACE_ANIMALS_INFO__", output))

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
