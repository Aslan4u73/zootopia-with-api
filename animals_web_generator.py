import data_fetcher


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
    animal_name = input("Please enter an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)

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
