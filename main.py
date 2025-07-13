from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Ты дружелюбный ассистент."},
        {"role": "user", "content": "Привет!"},
    ]
)

print(response.choices[0].message.content)
