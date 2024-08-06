import requests

API_KEY = "zc8ABBjwLG9RNUZACrQN63dBk3uTTCvRKmQWR5eb"
SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def search_food(query)
    params = {
        "api_key": API_KEY,
        "query": query,
        "pageSize": 5
    }
    response = requests.get(SEARCH_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


    