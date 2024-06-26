import subprocess
import time
import sys

# Demander à l'utilisateur un nom de domaine
domaine = input("Veuillez entrer un nom de domaine à énumérer : ")

# Construire la commande Nikto
commande = f"nikto -h {domaine}"

# Animation de chargement
print("Début du scan avec Nikto...")
animation = "|/-\\"
for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

# Exécuter la commande
processus = subprocess.Popen(commande, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Obtenir la sortie standard et les erreurs
sortie, erreur = processus.communicate()

# Enregistrer la sortie dans un fichier
with open('nikto.txt', 'w') as f:
    f.write(sortie.decode())

# Afficher le message de fin
print("\033[92mNikto a fini le scan\033[0m")

# Afficher les erreurs, le cas échéant
if erreur:
    print("Erreur :")
    print(erreur.decode())
