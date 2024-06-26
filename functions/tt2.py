from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import os
import webbrowser

def generate_pdf(input_file, output_file, title):

    # Ajoute les informations DNS du fichier dns_info.txt
    with open('report-analyse/dns_info.txt', 'r') as dns_file:
        dns_info = dns_file.read()

    # Ajoute les informations des sous-domaines du fichier subdomains.txt
    with open('report-analyse/subdomains.txt', 'r') as subdomains_file:
        subdomains_info = subdomains_file.read()
    
      # Ajoute les informations des sous-domaines du fichier subdomains.txt
    with open('report-analyse/robots.txt', 'r') as robots:
        robots = robots.read()

       # Ajoute les informations des sous-domaines du fichier subdomains.txt
    with open('report-analyse/dns.txt', 'r') as dnsrec:
        dnsrec = dnsrec.read()
    # Ajoute les informations des sous-domaines du fichier subdomains.txt
    with open('report-analyse/dnsrecon.txt', 'r') as dnsrecon:
        dnsrecon = dnsrecon.read()
     # Ajoute les informations des sous-domaines du fichier subdomains.txt
    with open('report-analyse/tech_web.txt', 'r') as tech_web:
        tech_web = tech_web.read()

    # Encadre le texte avec des balises <pre> pour créer un bloc de texte préformaté
    dnsrec = f"<pre>\n{dnsrec}\n</pre>"
    dns_info = f"<pre>\n{dns_info}\n</pre>"
    subdomains_info = f"<pre>\n{subdomains_info}\n</pre>"
    robots = f"<pre>\n{robots}\n</pre>"
    dnsrecon = f"<pre>\n{dnsrecon}\n</pre>"
    tech_web = f"<pre>\n{tech_web}\n</pre>"

    # Charge le modèle Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('functions/template.html')

    # Remplit le modèle avec le contenu, le titre, les informations DNS et les informations des sous-domaines
    html = template.render(title=title, dns_info=dns_info, subdomains_info=subdomains_info, robots=robots, dnsrec=dnsrec, dnsrecon=dnsrecon, tech_web=tech_web)

    # Crée un objet HTML avec WeasyPrint
    html_obj = HTML(string=html)

    # Ajoute un style CSS pour le titre, le numéro de page et le retour à la ligne automatique
    css = CSS(string='''
        @page {
            size: A4;
            margin: 1cm;
            @bottom-left {
                content: element(baspage);
            }
            @bottom-right {
                content: counter(page);
                font-size : 10px;
            }
            @bottom-center {
              content: element(entreprise);
            }
        }
              
        #titre {
              position : center;
              font-size: 20px;
              font-weight: bold;
              }

        #baspage {
            position: running(baspage);
            font-size: 10px;
            opacity:0.8;
            color : gray;
        }
        #entreprise {
              position: running(entreprise);
              font-size : 10px;
              opacity: 0.8;
              color : gray;
              }
        
        #scan {
              font-size : 10px;}
        #scan h2{
              font-size : 12px;}

        pre {
            white-space: pre-wrap;       /* CSS 3 */
            word-wrap: break-word;       /* Internet Explorer 5.5+ */
        }
    ''')

    # Génère le PDF
    html_obj.write_pdf(output_file, stylesheets=[css])
    
    webbrowser.open_new_tab(output_file)
# Utilisation de la fonction
generate_pdf('report-analyse/rapport.txt', 'report-analyse/rapport.pdf', "Rapport de l'analyse automatisé")
