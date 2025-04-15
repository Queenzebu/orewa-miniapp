from flask import Flask, request, jsonify
import telegram
import os

# Fetch Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Ensure this is correctly set in the environment variables
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to OREWA App!"  # Simple homepage message

# Set the webhook for Telegram updates
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = request.json  # Get the incoming update data from Telegram
        chat_id = update['message']['chat']['id']  # Get the chat ID of the sender
        message = update['message']['text']  # Get the text message sent by the user

        # Example response: Echo the received message (you can customize this)
        bot.send_message(chat_id=chat_id, text=f"You said: {message}")

        return jsonify(status="ok")  # Return an HTTP response to Telegram
    except Exception as e:
        return jsonify(error=str(e))  # Return any error that occurred during webhook handling

# Set the Telegram bot webhook (run this part once to set the webhook)
@app.route("/set_webhook", methods=["GET"])  # A route to set the webhook manually
def set_webhook():
    try:
        # Replace with your actual Render URL for the webhook
        webhook_url = "https://orewa-miniapp.onrender.com/webhook"  # Use your Render URL here
        bot.set_webhook(url=webhook_url)  # Set the webhook URL with Telegram
        return "Webhook has been set!"  # Success message
    except Exception as e:
        return jsonify(error=str(e))  # If there's an error, return the error message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)  # Run the Flask app
