import requests

token = "BQBv2jX3-1KY_YjaI4SIPv9oVeKdUmoMnftYfpGqNAkpysH1xgH5-oSP75KJmbNPpEgnRS_qhirf23Q4_218-S18Pq4s5Y8bwJkSmQmJtkbVlJhZetuyrk27qYM4fq1ZAG8Tf-ocBbY"

query = "rory in early 20s"
url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=5"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
data = response.json()

for item in data["tracks"]["items"]:
    print(item["name"], "-", item["artists"][0]["name"])
