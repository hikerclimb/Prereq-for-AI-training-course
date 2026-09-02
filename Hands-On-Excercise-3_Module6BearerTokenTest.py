import requests

url = "http://127.0.0.1:9006/api/protected"
payload = {
    "name": "Alice",
    "role": "admin"
}

# The requests library automatically adds 'Content-Type: application/json' when using json=
response = requests.post(url, json=payload)
print(response)