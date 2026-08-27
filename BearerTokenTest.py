import requests

BASE_URL = "http://127.0.0.1:8005"
TOKEN = "my-secret-token"

# 1. Test Public Endpoint
print("--- Testing Public Endpoint ---")
res_public = requests.get(f"{BASE_URL}/api/public")
print(f"Status: {res_public.status_code} | Response: {res_public.json()}\n")

# 2. Test Protected Endpoint WITHOUT a token (Should fail)
print("--- Testing Protected Endpoint (No Token) ---")
res_no_token = requests.get(f"{BASE_URL}/api//protected")
print(f"Status: {res_no_token.status_code} | Response: {res_no_token.json()}\n")

# 3. Test Protected Endpoint WITH a valid token (Should succeed)
print("--- Testing Protected Endpoint (Valid Token) ---")
headers = {"Authorization": f"Bearer {TOKEN}"}
res_auth = requests.get(f"{BASE_URL}/api/protected", headers=headers)
print(f"Status: {res_auth.status_code} | Response: {res_auth.json()}\n")