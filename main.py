from openai import OpenAI
from dotenv import load_dotenv
import base64

client = OpenAI()

def main(image):
    with open("image_path", "rb") as image:
        base64_image = base64.b64encode(image.read()).decode('utf-8')


    response = client.chat.completions.create(
        model="gpt-4o"
        messages=[
                {
                    "role":"user", 
                    "content": [
                        {
                            "type": "text",
                            "text": "How much calories this meal have?"
                        },
                        {
                            "type": "image_url",
                            "data": "data: image/jpeg;base64," + base64_image
                        }
                    ]

                },  
        ],
    )