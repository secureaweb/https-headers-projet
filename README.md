# https-headers-projet
🌐 HTTP & Headers Analyzer
📌 Description
Outil Python permettant d’envoyer une requête HTTP vers un site web et d’analyser les headers de réponse afin d’étudier les informations techniques et de sécurité exposées par un serveur.

🎯 Objectif
Comprendre le protocole HTTP
Analyser les headers de réponse serveur
Identifier les éléments liés à la sécurité web
Développer une première approche d’audit web

💻 Technologies
Python
requests
Replit (environnement de développement)

▶️ Utilisation
python main.py

💻 Code principal
import requests

url = "https://secureaweb.fr"

response = requests.get(url)
headers = response.headers

print("URL :", url)

for key, value in headers.items():
print(key, ":", value)

📊 Exemple de résultat
Content-Type : text/html
Permissions-Policy : …
Connection : keep-alive
Transfer-Encoding : chunked

🧠 Analyse sécurité
Identification des headers de sécurité présents
Détection de headers manquants (CSP, HSTS, X-Frame-Options)
Compréhension des risques liés à la configuration serveur

⚠️ Note
Projet réalisé dans un cadre d’apprentissage en cybersécurité, uniquement sur des cibles autorisées (sur mon propre site web)

🚀 Améliorations possibles
Détection automatique des headers manquants
Score de sécurité du site
Scan de plusieurs URLs
Export des résultats en fichier
