import requests

# NOTE: A Good Request
r = requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=10)
print(r.json())
print(r.json()["userId"])
print(r.status_code)
print(r.headers)

# NOTE: A Bad Request
bad = requests.get("https://jsonplaceholder.typicode.com/postss/1",timeout=10)
print(bad.status_code)
print(bad.json()) 

