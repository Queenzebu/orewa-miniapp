from flask import Flask, request, jsonify
import telegram
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Make sure this is set correctly
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Welcome message
welcome_text = (
    "👋 *Welcome to Orewapp!* 🚀🌍\n\n"
    "Orewapp is your all-in-one Web3 dashboard — built for mining, staking, NFTs, governance, and community-powered rewards — all inside Telegram!\n\n"
    "We’re on a mission to reward you for everything you do — from mining and farming, to voting and playing.\n\n"
    "Here’s what you can do with Orewapp right now:\n"
    "⛏️ *Start Mining:* Earn OREWA by tapping into daily mining sessions\n"
    "💰 *Stake & Farm:* Lock your tokens or LP to earn even more rewards\n"
    "🎨 *Collect NFTs:* Unlock boosts, voting power, and premium perks\n"
    "📢 *Complete SocialFi Quests:* Earn ZIPP for engaging on socials\n"
    "🪂 *Claim Airdrops:* Track your rewards from campaigns, beta tests, and more!\n\n"
    "New to the app? No worries — the dashboard guides you every step of the way 💡\n"
    "And don’t forget to check if you’re eligible for airdrops and Vanguard perks 👑\n\n"
    "🌐💎 *Welcome to the Orewa ecosystem — where your activity truly pays off!*"
)

@app.route("/")
def index():
    return "OREWA bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()

    # Handle callback query (button click)
    if "callback_query" in update:
        callback_query = update["callback_query"]
        user_id = callback_query["from"]["id"]
        data = callback_query["data"]

        if data == "launch_app":
            bot.send_message(chat_id=user_id, text="🚀 Loading your dashboard...", parse_mode="Markdown")
        return jsonify(status="callback received")

    # Handle normal message (/start)
    if "message" in update:
        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            bot.send_message(
                chat_id=chat_id,
                text=welcome_text,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("Launch App", callback_data="launch_app"),
                        InlineKeyboardButton("Join Community", url="https://t.me/OrevaAppOfficial")
                    ]
                ])
            )

    return jsonify(status="ok")

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://your-deployed-url/webhook"  # Change to your actual deployed URL
    success = bot.set_webhook(url=webhook_url)
    return "Webhook set!" if success else "Failed to set webhook"

if __name__ == "__main__":
    app.run(debug=True)
