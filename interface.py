import requests

url = "https://api.restful-api.dev/objects"

#GET
response = requests.get(url)
print(response.status_code)
print(response.json())


#POST(1)
payload = {
    "name": "Laptop",
    "data": {
        "price" : 80000,
        "brand" : "Dell",
    }
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())


#POST(2)
payload = {
    "name": "Mobile",
    "data": {
        "price" : 8000,
        "brand" : "LAVA",
    }
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())


#PUT
url = "https://api.restful-api.dev/objects/ff8081819782e69e019bb6e4fd622f07"

payload = {
    "name": "Updated Laptop",
    "data": {
        "price" : 85000
    }
}
response = requests.put(url, json=payload)
print(response.status_code)
print(response.json())


#DELETE
url = "https://api.restful-api.dev/objects/ff8081819782e69e019bb6e8ebe22f1c"

response = requests.delete(url, json=payload)
print(response.status_code)
print(response.json())


#PATCH
url = "https://api.restful-api.dev/objects/ff8081819782e69e019bb647ae982ca7"

payload = {
    "name": "Updated Name"
}

response = requests.patch(url, json=payload)
print(response.status_code)
print(response.json())


#HEAD
url = "https://api.restful-api.dev/objects"

response = requests.head(url)
print(response.status_code)
print(response.headers)


#TRACE
url = "https://api.restful-api.dev/objects"

response = requests.request("TRACE",url)
print(response.status_code)
print(response.text)


#OPTIONS
url = "https://api.restful-api.dev/objects"

response = requests.options(url)
print(response.status_code)
print(response.headers.get("Allow"))