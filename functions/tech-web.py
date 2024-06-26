import builtwith
import os
import sys

print("Analyse des techno Web en cours...")
# Vérifier si un nom de domaine a été passé en argument
if len(sys.argv) != 2:
    print("Usage : python3 script.py nomdedomaine")
    sys.exit(1)

# Le nom de domaine est le premier argument de la ligne de commande
domaine = sys.argv[1]

# Ajouter les préfixes http:// et https:// au nom de domaine
urls = [f"https://{domaine}"]

for url in urls:
    # Obtenir les informations sur les technologies utilisées par le site web
    info = builtwith.parse(url)

    # Créer le dossier report-analyse s'il n'existe pas
    if not os.path.exists('report-analyse'):
        os.makedirs('report-analyse')

    # Ouvrir le fichier de rapport pour écrire les résultats
    with open(f'report-analyse/tech_web.txt', 'a') as f:
        f.write(f"Résultats pour {url} :\n")
        for technologie, versions in info.items():
            f.write(f"{technologie} : {versions}\n")
        f.write("\n")

print("Analyse des techno Web terminé")
