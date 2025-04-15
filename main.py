from flask import Flask, request, jsonify
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

# Fetch Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to OREWA App!"

# Webhook to receive Telegram updates
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id

        if update.message:
            text = update.message.text

            if text == "/start":
                # Create buttons
                keyboard = [
                    [InlineKeyboardButton("🔗 Connect TON Wallet", callback_data="connect_wallet")],
                    [InlineKeyboardButton("📊 View Dashboard", callback_data="view_dashboard")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                bot.send_message(chat_id=chat_id,
                                 text="👋 Welcome to *OREWA Mini App!*\nChoose an option below:",
                                 reply_markup=reply_markup,
                                 parse_mode="Markdown")
            else:
                # Default response
                bot.send_message(chat_id=chat_id, text=f"You said: {text}")

        elif update.callback_query:
            data = update.callback_query.data
            if data == "connect_wallet":
                bot.send_message(chat_id=chat_id, text="🔗 Please connect your TON Wallet here: https://tonkeeper.app")
            elif data == "view_dashboard":
                bot.send_message(chat_id=chat_id, text="📊 Dashboard coming soon! Stay tuned.")
            else:
                bot.send_message(chat_id=chat_id, text="❓ Unknown action.")

        return jsonify(status="ok")
    except Exception as e:
        return jsonify(error=str(e))

# Manually set the webhook
@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    try:
        webhook_url = "https://orewa-miniapp.onrender.com/webhook"  # Replace with your actual URL
        bot.set_webhook(url=webhook_url)
        return "Webhook has been set!"
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
