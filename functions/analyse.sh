#!/bin/bash

REPORT_DIR="report-analyse"

# Créez le dossier de rapport s'il n'existe pas
mkdir -p $REPORT_DIR

# Demandez l'adresse IP ou le nom de domaine à l'utilisateur
read -p "Veuillez entrer l'adresse IP ou le nom de domaine : " TARGET

python3 functions/dnsrec.py $TARGET
python3 functions/dd.py $TARGET
python3 functions/sub.py $TARGET
python3 functions/robot.py $TARGET
dnsrecon -d $TARGET > report-analyse/dnsrecon.txt
python3 functions/tech-web.py $TARGET

#convertir le rapport Markdown en format PDF avec markdown-pdf
echo "Convertir le rapport Markdown en format PDF..."
python3 functions/tt2.py "${REPORT_DIR}/rapport.md" $REPORT

echo "Rapport généré: ${REPORT}"
