import requests

payload = {"title": "zxc", "body": "zxc"}
resp = requests.post("http://127.0.0.1:8000/notes", json=payload)
print(resp.status_code, resp.json())