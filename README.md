# ARR Missing Searcher 📥

**ARR Missing Searcher** est un outil qui automatise la recherche des séries et films manquants dans vos bibliothèques gérées par **Sonarr** et **Radarr**. Il interagit avec leurs API pour garder vos collections complètes et à jour, simplifiant ainsi la gestion de vos contenus multimédias.

## Prérequis ⚙️

Avant d'utiliser le script, assurez-vous d'avoir :

- **Python 3.x** installé.
- Les bibliothèques Python nécessaires installées :
  ```bash
  pip install requests
  ```

- Un serveur **Sonarr** et **Radarr** fonctionnel avec les **API activées**. Vous aurez besoin de l'URL de votre instance Sonarr/Radarr et de la clé API respective.

## Configuration ⚡

1. Clonez ou téléchargez ce dépôt :
   ```bash
   git clone https://github.com/Limoniak/arr-missing-searcher.git
   cd arr-missing-searcher
   ```

2. Ouvrez les scripts et remplissez les informations suivantes :

   - **Sonarr** :
     - `sonarr_url`: URL de votre serveur Sonarr (par exemple, `http://localhost:8989`).
     - `sonarr_api_key`: La clé API de votre instance Sonarr.

   - **Radarr** :
     - `radarr_url`: URL de votre serveur Radarr (par exemple, `http://localhost:7878`).
     - `radarr_api_key`: La clé API de votre instance Radarr.

## Utilisation 🚀

### Pour Sonarr & Radarr 🎬
Le script vérifiera les films/séries manquantes et lancera une recherche pour chaque film/épisode manquant.

```bash
python sonarr_missing_searcher.py
python radarr_missing_searcher.py
```

## Planification 🕓

Exemple de cron job (toutes les heures) :
```bash
0 * * * * /usr/bin/python3 /path/to/sonarr_missing_searcher.py
0 * * * * /usr/bin/python3 /path/to/radarr_missing_searcher.py
```

## Contribuer 🤝

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à ouvrir un **issue** ou à soumettre une **pull request**.

## Licence 📄

Ce projet est sous la licence MIT.

---

### Quelques conseils 💡 :

1. Assurez-vous de configurer correctement vos URLs et clés API avant d'exécuter le script.
2. Planifiez l'exécution régulière des scripts pour garantir que vos bibliothèques restent à jour avec les derniers épisodes et films.
