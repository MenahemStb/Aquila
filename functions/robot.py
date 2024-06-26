import requests
import sys
import re
import os

def get_robots_txt(domain):
    # Construit l'URL du fichier robots.txt
    robots_url = f"https://{domain}/robots.txt"

    try:
        # Télécharge le fichier robots.txt
        response = requests.get(robots_url)

        if response.status_code == 200:
            # Analyse le fichier robots.txt
            rules = re.findall(r"(User-agent|Disallow|Allow):\s*(\S*)", response.text, re.I)
            with open('report-analyse/robots.txt', 'w') as f:  # Ajouté ici
                f.write("User-agent et règles d'accès :\n")
                for rule in rules:
                    f.write(f"{rule[0]}: {rule[1]}\n")
        else:
            print(f"Erreur lors du téléchargement du fichier robots.txt. Code de statut HTTP : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à {robots_url} : {e}")

# Utilisation de la fonction
if len(sys.argv) > 1:
    domain = sys.argv[1]  # Utilisez le domaine fourni en argument
    get_robots_txt(domain)
else:
    print("Veuillez fournir un domaine en argument lors de l'exécution du script.")
