import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def get_calories(food_item):
  nutritionix_app_id = os.getenv('NUTRITIONIX_APP_ID')
  nutritionix_api_key = os.getenv('NUTRITIONIX_API_KEY')

  headers = {
    'x-app-id': nutritionix_app_id,
    'x-app-key': nutritionix_api_key
  }

  url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

  data = {
    'query': food_item,
    'locale': 'en_US'
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
    content = json.loads(response.content)
    print(json.dumps(content, indent=4))  # Print the JSON response nicely formatted
    return content
  else:
    print(f"Error: {response.status_code}")
    return None

if __name__ == "__main__":
  food_item = input("Enter a food item: ")
  get_calories(food_item)
