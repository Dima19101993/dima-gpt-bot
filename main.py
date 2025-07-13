from openai import OpenAI
import os
from pyTelegramBotAPI import telebot

# Ключи из переменных окружения
api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("TELEGRAM_TOKEN")

client = OpenAI(api_key=api_key)
bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши мне любой вопрос.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message.text}
    ]
)
answer = response.choices[0].message.content.strip()
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

bot.infinity_polling()
