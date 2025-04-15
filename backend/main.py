from flask import Flask, request, jsonify
import os
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import logging

# Set up Flask app and Telegram Bot
app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Welcome message text
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

# Handle /start command
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.message:
        chat_id = update.message.chat.id
        username = update.message.chat.username or "there"
        keyboard = [
            [InlineKeyboardButton("🚀 Launch App", callback_data="launch_app")],
            [InlineKeyboardButton("👥 Join Community", url="https://t.me/OrevaAppOfficial")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id=chat_id,
            text=welcome_text.replace("Welcome to Orewapp", f"Welcome {username} to Orewapp"),
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_markup=reply_markup
        )

    elif update.callback_query:
        query = update.callback_query
        data = query.data
        if data == "launch_app":
            bot.send_message(
                chat_id=query.message.chat_id,
                text="📊 Dashboard coming soon! Stay tuned."
            )
        bot.answer_callback_query(callback_query_id=query.id)

    return jsonify(status="ok")

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    webhook_url = "https://orewa-miniapp.onrender.com/webhook"  # <-- Your actual URL
    bot.set_webhook(url=webhook_url)
    return "Webhook has been set!"

@app.route("/")
def index():
    return "Welcome to OREWA MiniApp!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
