import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()  # Load environment variables from .env

def get_calories(food_item):
  nutritionix_app_id = os.getenv('NUTRITIONIX_APP_ID')
  nutritionix_api_key = os.getenv('NUTRITIONIX_API_KEY')

  headers = {
    'x-app-id': nutritionix_app_id,
    'x-app-key': nutritionix_api_key
  }

  url = 'https://api.nutritionix.com/v2/natural/nutrients'

  data = {
    'query': food_item,
    'locale': 'en_US'
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
    content = json.loads(response.content)
    try:
      calories = content['foods'][0]['nutrients'][0]['value']
      return calories
    except (IndexError, KeyError):
      return None  # Handle cases where data is missing or incorrect
  else:
    return None  # Handle API errors

def calorie_counter():
  total_calories = 0
  while True:
    food = input("Enter a food (or 'quit' to exit): ").lower()
    if food == 'quit':
      break
    calories = get_calories(food)
    if calories:
      total_calories += calories
      print(f"{food} added. Total calories: {total_calories}")
    else:
      print("Food not found or error occurred.")

  print("\nTotal calorie intake:", total_calories)

if __name__ == "__main__":
  calorie_counter()
