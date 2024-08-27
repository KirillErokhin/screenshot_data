import os
import base64

from openai import OpenAI

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_data_chatgpt(TOKEN, BASE_URL, image_path):
    client = OpenAI(api_key=TOKEN, base_url=BASE_URL)
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "Тебе на вход идет скриншот экрана. Выведи мне ТОЛЬКО дату и время на этом скриншоте в формате ДД.ММ.ГГГГ ЧЧ:ММ. Если даты и времени нет, выведи None"},
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                },
                },
            ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content