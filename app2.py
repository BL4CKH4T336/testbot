from flask import Flask
import telebot
import threading

API_TOKEN = '7893130831:AAFqjiwzUyXNQbNYuSt0rWT9Ex8J_S2qG9Y'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Delete webhook before starting polling
bot.remove_webhook()

# Telegram bot handler
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "I am running")

# Flask route
@app.route('/')
def home():
    return "Flask app is running!"

def run_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=5000)
