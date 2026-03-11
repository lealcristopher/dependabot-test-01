import requests

def get_google_status():
    response = requests.get("https://www.google.com")
    return response.status_code