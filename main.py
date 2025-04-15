from flask import Flask, request, jsonify
import telegram
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Detailed welcome message
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
def home():
    return "Welcome to OREWA App!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    chat_id = update['message']['chat']['id']
    message = update['message']['text']

    # Respond to /start command
    if message == "/start":
        # Send welcome message with options
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

    # Handle callback query for "Launch App" button
    if "callback_query" in update:
        callback_data = update['callback_query']['data']
        user_id = update['callback_query']['from']['id']  # Get the user's id
        if callback_data == "launch_app":
            # Check if callback_data is received correctly
            bot.send_message(chat_id=user_id, text="Launching your app... 🚀")
            # Optional: Add more functionality for the "Launch App" action

    return jsonify(status="ok")

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://your-app-url/webhook"  # Replace with your actual URL
    bot.set_webhook(url=webhook_url)
    return "Webhook has been set!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
