import socket
import requests
import sys

def handler(url):
    print("Collecte DNS-Server en cours...")
    try:
        # Supprime le protocole de l'URL pour obtenir le domaine
        domain = url.replace("http://", "").replace("https://", "")

        # Utilisez socket pour obtenir les adresses IP associées au domaine
        addresses = socket.gethostbyname_ex(domain)[2]

        results = []
        for address in addresses:
            # Utilisez socket pour obtenir le nom d'hôte associé à l'adresse IP
            try:
                hostname = socket.gethostbyaddr(address)[0]
            except socket.herror:
                hostname = None

            # Vérifiez si l'adresse IP prend en charge DNS over HTTPS (DoH)
            try:
                response = requests.get(f"https://{address}/dns-query")
                doh_direct_supports = response.status_code == 200
            except requests.exceptions.RequestException:
                doh_direct_supports = False

            results.append({
                "address": address,
                "hostname": hostname,
                "dohDirectSupports": doh_direct_supports,
            })

        data = {
            "domain": domain,
            "dns": results,
        }

        # Écrire les données dans un fichier txt
        with open('report-analyse/dns_info.txt', 'w') as f:
            f.write(f"Domaine : {data['domain']}\n")
            for i, result in enumerate(data['dns'], start=1):
                f.write(f"\nRésultat DNS {i} :\n")
                f.write(f"Adresse : {result['address']}\n")
                f.write(f"Nom d'hôte : {result['hostname']}\n")
                f.write(f"Supporte DoH directement : {'Oui' if result['dohDirectSupports'] else 'Non'}\n")

        return data
    except Exception:
        pass

# Utilisation de la fonction
if len(sys.argv) > 1:
    handler(sys.argv[1])
