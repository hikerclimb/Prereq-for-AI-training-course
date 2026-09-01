import requests

BASE_URL = "https://428331109880-13uguscasnu19cqm1b6ck2f5l6gl1885.apps.googleusercontent.com" #"https://gmail.googleapis.com/gmail/v1/users"
#should store token in a file
TOKEN = "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"

# 1. Test Public Endpoint
'''print("--- Testing Public Endpoint ---")
res_public = requests.get(f"{BASE_URL}/api/public")
print(f"Status: {res_public.status_code} | Response: {res_public.json()}\n")

# 2. Test Protected Endpoint WITHOUT a token (Should fail)
print("--- Testing Protected Endpoint (No Token) ---")
res_no_token = requests.get(f"{BASE_URL}/api//protected")
print(f"Status: {res_no_token.status_code} | Response: {res_no_token.json()}\n")
'''
#3. Test Protected Endpoint WITH a valid token (Should succeed)
print("--- Testing Protected Endpoint (Valid Token) ---")
headers = {"Authorization": f"Bearer {TOKEN}"}
res_auth = requests.get(f"{BASE_URL}", headers=headers)
print(f"Status: {res_auth.status_code}")

'''try:
    # Try to print the JSON if it exists
    print(f"Response (JSON): {res_auth.json()}\n")
except requests.exceptions.JSONDecodeError:
    # If it fails, print the raw text to see the actual error message or HTML
    print(f"Response (Raw Text): {res_auth.text}\n")
'''
