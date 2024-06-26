#!/bin/bash
# Fonction pour afficher le menu de reconnaissance
afficher_menu_reco() {
    echo "Menu Enumeraiton :"
    # Ajoutez ici les options spécifiques à la reconnaissance
    echo "1. Enumeration complète d'une cible"
    echo "2. Enumeration Nmap Brute"
    echo "2. Enumeration Nmap nikto"

}

# Boucle pour afficher le menu de reconnaissance en continu
while true; do
    afficher_menu_reco
    read -p "Choisissez une option (1-3) : " choix_options

    case "$choix_options" in
        1)
            echo "Debuter l'enumération complète sur une cible"
            # Ajoutez ici le code pour l'option 1 de reconnaissance
            ;;
        2)
            echo "Enumeration Nmap Brute"
            # Sort de la boucle pour revenir au menu principal
            ;;
        3)
            echo "Retour au menu principal."
            break  # Sort de la boucle pour revenir au menu principal
            ;;
        *)
            echo "Option invalide. Veuillez choisir une option valide (1-3)."
            ;;
    esac
done
