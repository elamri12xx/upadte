
import requests

url = "https://api-v2.fallakatv.eu.org/france.php"
response = requests.get(url)

with open("france.json", "w", encoding="utf-8") as f:
    f.write(response.text)
