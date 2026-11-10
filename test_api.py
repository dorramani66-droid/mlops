import requests

URL = "http://localhost:8000"

# ===== 1. Vérifier que l'API fonctionne =====
print("GET /health ->", requests.get(URL + "/health").json())

# ===== 2. Tester avec un client à faible consommation =====
client = {
    "age": 35,
    "salaire": 2500,
    "abonnement": "Standard",
    "anciennete": 1,
    "consommation": 10
}

r = requests.post(URL + "/predict", json=client)
print("POST /predict (client 1) ->", r.status_code, r.json())