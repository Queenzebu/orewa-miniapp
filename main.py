from flask import Flask, request, jsonify
import telegram
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to OREWA App!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    chat_id = update['message']['chat']['id']
    message = update['message']['text']

    # Respond to /start command
    if message == "/start":
        welcome_message = f"""
        Welcome {update['message']['from']['username']}! 🚀
        
        Please connect your wallet later.
        
        Choose one of the options below:
        
        1️⃣ Launch App
        2️⃣ Join Community
        """
        
        # Define the inline buttons
        keyboard = [
            [
                InlineKeyboardButton("Launch App", callback_data="launch_app"),
                InlineKeyboardButton("Join Community", url="https://t.me/OrevaAppOfficial")
            ]
        ]
        
        # Send the welcome message with inline buttons
        bot.send_message(
            chat_id=chat_id,
            text=welcome_message,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    return jsonify(status="ok")

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://your-app-url/webhook"  # Replace with your actual URL
    bot.set_webhook(url=webhook_url)
    return "Webhook has been set!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
