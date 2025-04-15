from flask import Flask, request, jsonify
import telegram
import os

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

    if message == "/start":
        welcome_message = """
        Welcome {0}! 🚀
        
        Please connect your wallet later.
        
        Choose one of the options below:
        
        1️⃣ Launch App
        2️⃣ Join Community
        """.format(update['message']['from']['username'])
        
        # Sending the welcome message with options
        bot.send_message(
            chat_id=chat_id,
            text=welcome_message,
            reply_markup=telegram.inline.KeyboardButton([
                [
                    telegram.InlineKeyboardButton("Launch App", callback_data="launch_app"),
                    telegram.InlineKeyboardButton("Join Community", url="https://t.me/OrevaAppOfficial")
                ]
            ])
        )
    
    return jsonify(status="ok")

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://your-app-url/webhook"  # Replace with your actual URL
    bot.set_webhook(url=webhook_url)
    return "Webhook has been set!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
