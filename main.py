from flask import Flask, request, jsonify
import telegram
import os

# Fetch Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Store users in a dictionary for simplicity (you can later use a database)
users = {}

@app.route("/")
def home():
    return "Welcome to OREWA App!"

# Handle the '/start' command and capture the username
@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    chat_id = update['message']['chat']['id']
    message = update['message']['text']

    if message == "/start":
        # Capture Telegram username
        username = update['message']['from'].get('username', 'Anonymous')

        # Store username in the users dictionary
        users[chat_id] = {'username': username}

        # Send welcome message with options to connect wallet later
        bot.send_message(chat_id=chat_id, text=f"Welcome {username}! 🚀\n\nPlease connect your wallet later.\n\nChoose one of the options below:\n\n1️⃣ Launch App\n2️⃣ Join Community")
    
    elif message == "1️⃣ Launch App":
        # Proceed to the app after the user clicks Launch App
        bot.send_message(chat_id=chat_id, text="Welcome to the OREWA App Dashboard! 🎮💰")

    elif message == "2️⃣ Join Community":
        # Provide community details with the link
        bot.send_message(chat_id=chat_id, text="Join our community at: [https://t.me/OrevaAppOfficial](https://t.me/OrevaAppOfficial)")

    return jsonify(status="ok")

# Set the webhook for Telegram updates
@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://your-app-url/webhook"  # Replace with your actual URL
    bot.set_webhook(url=webhook_url)
    return "Webhook has been set!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
