import requests

# --- CONFIGURATION ---
RADARR_API_URL = "http://localhost:7878/api/v3/command"  # URL de l'API Radarr
RADARR_API_KEY = "VOTRE_API_KEY"  # Remplacez par votre clé API Radarr

def search_missing_movies():
    """
    Lance une recherche des films manquants via l'API de Radarr.
    """
    # Préparer la requête API
    endpoint = RADARR_API_URL
    headers = {
        "X-Api-Key": RADARR_API_KEY,  # Clé API pour authentification
    }
    payload = {
        "name": "MissingMoviesSearch",  # Commande pour rechercher les films manquants
    }

    try:
        # Envoyer la requête POST à Radarr
        response = requests.post(endpoint, json=payload, headers=headers)

        # Vérifier la réponse
        if response.status_code == 201:
            print("Recherche des films manquants lancée avec succès.")
        else:
            print(f"Erreur lors de la recherche : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exécuter la fonction
if __name__ == "__main__":
    search_missing_movies()
