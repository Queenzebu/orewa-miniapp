from flask import Flask, request, jsonify
import telegram
import os

# Fetch Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to OREWA App!"  # Simple homepage message

# Set the webhook for Telegram updates
@app.route("/webhook", methods=["POST"])  # Webhook route to handle incoming Telegram updates
def webhook():
    update = request.json  # Get the incoming update data from Telegram
    chat_id = update['message']['chat']['id']  # Get the chat ID of the sender
    message = update['message']['text']  # Get the text message sent by the user

    # Respond to the user: Echo the received message (you can customize this)
    bot.send_message(chat_id=chat_id, text=f"You said: {message}")
    
    return jsonify(status="ok")  # Return an HTTP response to Telegram

# Set the Telegram bot webhook (run this part once to set the webhook)
@app.route("/set_webhook", methods=["GET"])  # A route to set the webhook manually
def set_webhook():
    webhook_url = "https://orewa-miniapp.onrender.com/webhook"  # Replace with your actual URL (Render URL)
    bot.set_webhook(url=webhook_url)  # Set the webhook URL in Telegram
    return "Webhook has been set!"  # Inform you that the webhook has been set

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)  # Run the Flask app
