import requests #modul (get et post)
import hashlib #modul (hashage)
import re #modul (regex)

url = "https://docker.hackthebox.eu:31066"
s = requests.Session() # Debut de la session

### GET Request
out = s.get(url)
html = out.content

print(html)
"""
print(out)
out = re.search("<h3 align='center'>+.*?</h3>",out.text)
print(out)
"""
