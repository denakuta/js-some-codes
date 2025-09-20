import cloudscraper
from bs4 import BeautifulSoup
import json, csv

url = "https://ru.dotabuff.com/heroes"

scraper = cloudscraper.create_scraper()  # автоматически обрабатывает cloudflare/challenges
resp = scraper.get(url, timeout=20)
print("HTTP status:", resp.status_code)
html = resp.text

soup = BeautifulSoup(html, "lxml")

heroes = []
for a in soup.select("section a[href^='/heroes/'], a[href^='/heroes/']"):
    name = a.get_text(" ", strip=True)
    if name and name not in heroes:
        heroes.append(name)

print(f"Найдено {len(heroes)} героев")
for i,h in enumerate(heroes,1):
    print(i, h)

# Сохранение
with open("heroes.json", "w", encoding="utf-8") as f:
    json.dump(heroes, f, ensure_ascii=False, indent=2)

with open("heroes.csv", "w", encoding="utf-8", newline="") as f:
    import csv as _csv
    w = _csv.writer(f)
    w.writerow(["Имя героя"])
    for h in heroes:
        w.writerow([h])
