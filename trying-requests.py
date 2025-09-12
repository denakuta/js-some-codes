import requests

link = "http://127.0.0.1:8000/ping"
response = requests.get(link)
print(response.json())