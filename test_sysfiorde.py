import requests
from bs4 import BeautifulSoup

URL = ""

response = requests.get(
    URL,
    timeout=60,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("STATUS:", response.status_code)
print("TAMANHO HTML:", len(response.content))

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

print("TABELAS ENCONTRADAS:", len(tables))

for i, table in enumerate(tables):
    rows = table.find_all("tr")
    print(f"TABELA {i}: {len(rows)} linhas")
