import dns.resolver
import os
import sys

# Vérifier si un argument a été passé
if len(sys.argv) != 2:
    print("Usage: python script.py domaine")
    sys.exit(1)

# Définir la cible
TARGET = sys.argv[1]

# Créer le dossier de rapport s'il n'existe pas
REPORT_DIR = "report-analyse"
os.makedirs(REPORT_DIR, exist_ok=True)

# Définir le fichier de rapport
REPORT_FILE = os.path.join(REPORT_DIR, "dns.txt")

# Liste des types d'enregistrements à récupérer
record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME', 'SOA', 'SRV', 'PTR']
print("Collecte DNS en cours...")
with open(REPORT_FILE, 'w') as f:
    for record_type in record_types:
        f.write(f"Enregistrements {record_type} :\n")
        try:
            answers = dns.resolver.resolve(TARGET, record_type)
            for rdata in answers:
                f.write(str(rdata) + "\n")
        except dns.resolver.NoAnswer:
            f.write("Pas de réponse\n")
        except dns.resolver.NXDOMAIN:
            f.write("Domaine non existant\n")
        f.write("\n")
