from flask import Flask, request, jsonify
import telegram
import os

# Fetch Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to OREWA App!"

# Set the webhook for Telegram updates
@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    # This is where you'll process the updates
    chat_id = update['message']['chat']['id']
    message = update['message']['text']

    # Example response: Echo the received message
    bot.send_message(chat_id=chat_id, text=f"You said: {message}")
    
    return jsonify(status="ok")

# Set the Telegram bot webhook (run this part once to set the webhook)
@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://your-app-url/webhook"  # Replace with your actual URL
    bot.set_webhook(url=webhook_url)
    return "Webhook has been set!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
