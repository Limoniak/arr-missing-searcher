# ARR Missing Searcher 📥

**ARR Missing Searcher** is a tool that automates the search for missing series and movies in your libraries managed by **Sonarr** and **Radarr**. It interacts with their APIs to keep your collections complete and up-to-date, simplifying the management of your multimedia content.

## Prerequisites ⚙️

Before using the script, ensure you have:

- **Python 3.x** installed.
- The required Python libraries installed:
  ```bash
  pip install requests
  ```

- A functional **Sonarr** and **Radarr** server with **APIs enabled**. You will need the URL of your Sonarr/Radarr instance and the respective API key.

## Configuration ⚡

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Limoniak/arr-missing-searcher.git
   cd arr-missing-searcher
   ```

2. Open the scripts and fill in the following information:

   - **Sonarr**:
     - `sonarr_url`: URL of your Sonarr server (e.g., `http://localhost:8989`).
     - `sonarr_api_key`: The API key for your Sonarr instance.

   - **Radarr**:
     - `radarr_url`: URL of your Radarr server (e.g., `http://localhost:7878`).
     - `radarr_api_key`: The API key for your Radarr instance.

## Usage 🚀

### For Sonarr & Radarr 🎬
The script will check for missing movies/series and initiate a search for each missing movie/episode.

```bash
python sonarr_missing_searcher.py
python radarr_missing_searcher.py
```

## Scheduling 🕓

Example of a cron job (every hour):
```bash
0 * * * * /usr/bin/python3 /path/to/sonarr_missing_searcher.py
0 * * * * /usr/bin/python3 /path/to/radarr_missing_searcher.py
```

## Contributing 🤝

Contributions are welcome! If you’d like to improve this project, feel free to open an **issue** or submit a **pull request**.

## License 📄

This project is licensed under the MIT License.

---

### Tips 💡:

1. Ensure you configure your URLs and API keys correctly before running the script.
2. Schedule regular execution of the scripts to ensure your libraries stay up-to-date with the latest episodes and movies.
