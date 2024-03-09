import requests
import json

url = "http://127.0.0.1:5000/food_product/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

payload = json.dumps({
  "label": "test",
  "category": "test",
  "price": 55
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


url = "http://127.0.0.1:5000/food_product/1"

payload = json.dumps({
  "label": "string",
  "category": "string",
  "price": 20
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

payload = ""
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

print("_______________________________________________________")
print("_______________________________________________________")
print("_______________________________________________________")
print("_______________________________________________________")

url = "http://127.0.0.1:5000/tech_product/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

payload = json.dumps({
    "label": "string",
    "category": "string",
    "description": "string",
    "brand": "string",
    "price": 30
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "http://127.0.0.1:5000/tech_product/1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


payload = json.dumps({
    "label": "modified",
    "category": "string",
    "description": "string",
    "brand": "string",
    "price": 60
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

payload = ""
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
