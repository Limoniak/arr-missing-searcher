import requests

# --- CONFIGURATION ---
SONARR_API_URL = "http://localhost:8989/api/v3/command"  # URL de l'API Sonarr
SONARR_API_KEY = "VOTRE_API_KEY"  # Remplacez par votre clé API Sonarr

def search_missing_episodes():
    """
    Lance une recherche des épisodes manquants via l'API de Sonarr.
    """
    # Préparer la requête API
    endpoint = SONARR_API_URL
    headers = {
        "X-Api-Key": SONARR_API_KEY,  # Clé API pour authentification
    }
    payload = {
        "name": "MissingEpisodeSearch",  # Commande pour rechercher les épisodes manquants
    }

    try:
        # Envoyer la requête POST à Sonarr
        response = requests.post(endpoint, json=payload, headers=headers)

        # Vérifier la réponse
        if response.status_code == 201:
            print("Recherche des épisodes manquants lancée avec succès.")
        else:
            print(f"Erreur lors de la recherche : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exécuter la fonction
if __name__ == "__main__":
    search_missing_episodes()
