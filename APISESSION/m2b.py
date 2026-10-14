import requests
records = [
    {
        "id" : 1,
        "name" : "Asha",
        "email" : "ASHAExample.com",
        "address" : {
            "city" : "Hyderabad"
        }
    },
    {
        "id" : 2,
        "name" : "Ravi",
        "email" : None,
        "address" : {
            "city" : "Pune"
        }
    },
    {
        "id" : 3,
        "name" : "Meera",
        "email" : "meera@example.com",
        "address" : {
            "city" : None
        }
    }
]

print(records)
var = requests.post("https://jsonplaceholder.typicode.com/posts/",json=records,timeout=10)
print(var)
print(var.status_code)
print(var.json())

for r in records : 
    print(f'{r["id"]},{r["name"]}')

# NOTE: TASK -> Null value vs Missing Value 
# NOTE: TASK -> Spaces in names what does happens if spaces are there in the name and searching
