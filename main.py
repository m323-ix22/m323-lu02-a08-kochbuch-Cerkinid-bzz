import json
from typing import Dict, Any


def load_recipe(json_string: str) -> Dict[str, Any]:
    """
    Wandelt einen JSON-kodierten String in ein Python-Dictionary um.
    """
    return json.loads(json_string)


def adjust_recipe(recipe: Dict[str, Any], num_people: int) -> Dict[str, Any]:
    """
    Passt die Mengenangaben eines Rezepts an die angegebene Anzahl von Personen an.
    """
    factor = num_people / recipe['servings']
    adjusted_ingredients = {
        ingredient: int(amount * factor)
        for ingredient, amount in recipe['ingredients'].items()
    }

    # Erstellen eines neuen, angepassten Rezepts
    adjusted_recipe = {
        "title": recipe['title'],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }

    return adjusted_recipe


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Rezept laden
    recipe = load_recipe(recipe_json)

    # Rezept an die Anzahl der Personen anpassen
    num_people = 2
    adjusted_recipe = adjust_recipe(recipe, num_people)

    # Ausgeben des angepassten Rezepts
    print(json.dumps(adjusted_recipe, indent=4))
