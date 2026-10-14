# NOTE:  Performing some more options on using the requests library
import requests

users = requests.get("https://jsonplaceholder.typicode.com/users",timeout=10).json()
print(type(users),len(users))
print(users[0])
print(users[0]['name'])
print(users[0]['address'])

print()
for user in users :
    print(f"|{user['name']} | {user['email']} | {user['address']['city']}|")

