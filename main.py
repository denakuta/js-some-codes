import base64
import requests

# Вставь свои данные
client_id = "0a45c244f4cc4773937ae950a7674fef"
client_secret = "870f91b488864f4392ec82f80f103c10"

# кодируем client_id:client_secret в base64
auth_str = f"{client_id}:{client_secret}"
b64_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Authorization": f"Basic {b64_auth}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {"grant_type": "client_credentials"}

r = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
print(r.json())