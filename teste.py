import requests

# Replace with your actual client ID and secret
client_id = 'QQbzJGSxo5MyNIJfkvH9HKgzqd0J21yqON7FypJJ'
client_secret = 'fECAIM7FqUunpnif1ABZUU7tzQ9cecHbf2mUbdJd1EkrXg6cW4p66mRpH6oxgaT9F1vaAkEPulWPSSvwXB9cAxjaJzJWUoasZuPP5qIqEFT3zrEjB9ziA5Ym7XqLEyfZ'

# Token endpoint
token_url = 'http://127.0.0.1:8000/o/token/'

# Data for token request
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

# Request the token
response = requests.post(token_url, data=data)
token = response.json().get('access_token')

# Use the token to access the protected API
headers = {'Authorization': f'Bearer {token}'}
api_url = 'http://127.0.0.1:8000/api/rooms'  # Replace with your actual API endpoint
api_response = requests.get(api_url, headers=headers)

print("Status:", api_response.status_code)
print("Resposta:", api_response.json())