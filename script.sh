#!/bin/bash

affichelogo() {
cat logo_ascii
}

# Fonction pour afficher le menu
afficher_menu() {
    affichelogo
    echo "Menu :"
    echo "1. Reconnaissance"
    echo "2. Avancés"
}

# Boucle pour afficher le menu en continu
while true; do
    afficher_menu
    read -p "Choisissez une option (1-2) ou 'q' pour quitter : " choix

    case "$choix" in
        1)
            echo "Vous avez choisi la reconnaissance."
            ./reco.sh
            ;;
        2)
            echo "Vous avez choisi les options avancées."
            ./options.sh
            ;;
        q)
            echo "Au revoir !"
            exit 0
            ;;
        *)
            echo "Option invalide. Veuillez choisir une option valide (1-2) ou 'q' pour quitter."
            ;;
    esac
done
