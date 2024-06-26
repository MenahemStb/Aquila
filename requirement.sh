#!/bin/bash

# Vérifier si nmap est installé
if command -v nmap >/dev/null 2>&1; then
    echo -e "\e[32mnmap est déjà installé\e[0m"
else
    echo "Installation de nmap..."
    sleep 2
    sudo apt-get install nmap -y
fi

# Installer les prérequis
echo "Installation des prérequis..."
sleep 2
pip install markdown weasyprint jinja2 dnspython

if [ $? -eq 0 ]; then
    echo -e "\e[32mLes prérequis ont été installés avec succès\e[0m"
else
    echo "Une erreur s'est produite lors de l'installation des prérequis"
    exit 1
fi

# Donner les droits d'exécution à tous les scripts .sh du dossier
echo "Configuration des scripts..."
chmod +x *.sh

if [ $? -eq 0 ]; then
    echo -e "\e[32mConfiguration terminée. Vous pouvez lancer l'outil en faisant ./script.sh\e[0m"
else
    echo "Une erreur s'est produite lors de la configuration des scripts"
    exit 1
fi
