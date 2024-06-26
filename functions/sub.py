import requests
import sys

def get_subdomains(domain):
    print("Collecte des Sous-Domaines en cours...")
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.ok:
            response_json = response.json()
            subdomains = set()
            for result in response_json:
                subdomains.add(result['name_value'])
            return sorted(subdomains)
    except requests.exceptions.RequestException:
        pass

# Utilisation de la fonction
if len(sys.argv) > 1:
    domain = sys.argv[1]  # Utilisez le domaine fourni en argument
    subdomains = get_subdomains(domain)
    if subdomains:
        with open('report-analyse/subdomains.txt', 'w') as f:
            for subdomain in subdomains:
                f.write(subdomain + '\n')
