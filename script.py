import requests
import re
from datetime import datetime
import os

date = datetime.strptime("2025-12-01", "%Y-%m-%d")

owner = "julian-u03"
repo = "autoupdate_from_github"
branch = "main"
filepath = "README.md"

url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{filepath}"

response = requests.get(url)

if response.status_code != 200:
    print("Fehler:", response.status_code)
    exit

readme_text = response.text

match = re.search(r'"(.*?)"', readme_text)
date_text = match.group(1)
date_latest_changes = datetime.strptime(date_text, "%Y-%m-%d")

if date_latest_changes > date:
    file_script = "script.py"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_script}"

    response = requests.get(url)

    with open(file_script, "wb") as f:
        f.write(response.content)

    os.startfile("script.py")