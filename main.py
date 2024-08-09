from openai import OpenAI
from dotenv import load_dotenv
import base64

client = OpenAI()

def get_calories_from_image(image_path):
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode('utf-8')


    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "How many calories is in this meal?"
                    },
                    {
                    "type": "image",
                    "image": "data:image/jpg;base64," + base64_image
                    }
                ]
            }  
        ],
    )
    response_message = response.choices[0].message
    content = response_message.content

    return content