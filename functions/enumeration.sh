#!/bin/bash

REPORT_DIR="reports"

# Créez le dossier de rapport s'il n'existe pas
mkdir -p $REPORT_DIR

# Demandez l'adresse IP ou le nom de domaine à l'utilisateur
read -p "Veuillez entrer l'adresse IP ou le nom de domaine : " TARGET
REPORT="${REPORT_DIR}/rapport.pdf"

# Animation de chargement
echo "Scan en cours..."
spin='-\|/'

# Effectuez une analyse de base avec nmap en arrière-plan
nmap -v -A $TARGET -oN "${REPORT_DIR}/rapport.txt" &> /dev/null &

# Obtenez l'ID du processus de nmap
NMAP_PID=$!

# Affichez une animation de chargement pendant que nmap est en cours d'exécution
i=0
while kill -0 $NMAP_PID 2>/dev/null
do
  i=$(( (i+1) %4 ))
  printf "\r${spin:$i:1}"
  sleep .1
done

# Convertir le rapport nmap en format Markdown
echo "Convertir le rapport nmap en format Markdown..."
echo "# Rapport Nmap pour ${TARGET}" > "${REPORT_DIR}/rapport.md"

# Convertir le rapport Markdown en format PDF avec markdown-pdf
echo "Convertir le rapport Markdown en format PDF..."
python3 tt3.py "${REPORT_DIR}/rapport.md" $REPORT

echo -e "\033[32mRapport généré: ${REPORT}\033[0m"