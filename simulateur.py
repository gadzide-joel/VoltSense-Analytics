import requests
import time
import random

# L'adresse de ton API locale
url = "http://127.0.0.1:8000/api/v1/telemetry"

print("Démarrage du simulateur VoltSense...")

while True:
    # Génération de fausses données réalistes
    voltage = round(random.uniform(210.0, 245.0), 1)
    current = round(random.uniform(1.2, 4.5), 2)
    power = round(voltage * current, 2)

    data = {
        "device_id": "Simulateur_PC",
        "voltage": voltage,
        "current": current,
        "power": power,
        "frequency": 50.0
    }

    try:
        response = requests.post(url, json=data)
        print(f"Relevé envoyé : {voltage}V, {current}A | Code serveur : {response.status_code}")
    except requests.exceptions.RequestException:
        print("Erreur : Impossible de joindre le serveur FastAPI.")

    # Attendre 5 secondes avant le prochain envoi
    time.sleep(5)
