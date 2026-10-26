import requests
try:
    r = requests.get("https://jsonplaceholder.typicode.com/postss", timeout=10)
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP problem:", e)
