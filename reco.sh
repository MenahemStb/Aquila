# Fonction pour afficher le menu de reconnaissance
afficher_menu_reco() {
    echo "Menu de reconnaissance :"
    # Ajoutez ici les options spécifiques à la reconnaissance
    echo "1. Debuter collecte d'information sur une cible"
    echo "2. Retour au menu principal"
}

# Boucle pour afficher le menu de reconnaissance en continu
while true; do
    afficher_menu_reco
    read -p "Choisissez une option (1-2) : " choix_reco

    case "$choix_reco" in
        1)
            echo "Debuter une reconnaissance sur une cible"
            # Ajoutez ici le code pour l'option 1 de reconnaissance
            bash functions/analyse.sh
            ;;
        2)
            echo "Retour au menu principal."
            break  # Sort de la boucle pour revenir au menu principal
            ;;
        *)
            echo "Option invalide. Veuillez choisir une option valide (1-3)."
            ;;
    esac
done
