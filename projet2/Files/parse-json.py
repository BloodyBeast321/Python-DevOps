import os
import json

def find_json_file(start_path="."):
    current_dir = os.path.abspath(start_path)

    for root, _, files in os.walk(current_dir):
        for file in files:
            if file.endswith(".json"):
                return os.path.join(root, file)
    return None

def parse_json_file(json_file_path):
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
        return None
    except json.JSONDecodeError:
        print("Erreur lors de la lecture du fichier JSON.")
        return None

def process_json_data(json_data):
    if json_data:
        # Extrait et affiche la valeur associée à la clé 'name'
        if 'name' in json_data:
            print(f"Valeur associée à la clé 'name' : {json_data['name']}")

        # Parcourt toutes les clés et valeurs du dictionnaire JSON
        print("Paires clé-valeur dans le dictionnaire JSON :")
        for key, value in json_data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    # Utilise la fonction find_json_file pour localiser un fichier JSON à partir du répertoire courant
    json_path = find_json_file()

    if json_path:
        print(f"Chemin du fichier JSON trouvé : {json_path}")

        # Utilise la fonction parse_json_file pour lire et charger le contenu du fichier JSON
        json_data = parse_json_file(json_path)

        # Traite les données dans le fichier JSON
        process_json_data(json_data)
    else:
        print("Aucun fichier JSON n'a été trouvé.")
