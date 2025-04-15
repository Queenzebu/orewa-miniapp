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

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id

        if update.message:
            text = update.message.text.strip().lower()

            if text == "/start":
                # ✨ Rich Welcome Message
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

                # 🔘 Updated buttons
                keyboard = [
                    [InlineKeyboardButton("🚀 Launch OREWA", callback_data="launch_orewa")],
                    [InlineKeyboardButton("👥 Join Community", url="https://t.me/OrevaAppOfficial")]  # replace this
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                bot.send_message(chat_id=chat_id,
                                 text=welcome_text,
                                 reply_markup=reply_markup,
                                 parse_mode="Markdown")
            else:
                bot.send_message(chat_id=chat_id, text=f"You said: {text}")

        elif update.callback_query:
            data = update.callback_query.data
            if data == "launch_orewa":
                bot.send_message(chat_id=chat_id, text="🚀 Launching dashboard... (coming soon!)")
            else:
                bot.send_message(chat_id=chat_id, text="❓ Unknown action.")

        return jsonify(status="ok")

    except Exception as e:
        return jsonify(error=str(e))

@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    try:
        webhook_url = "https://orewa-miniapp.onrender.com/webhook"
        bot.set_webhook(url=webhook_url)
        return "Webhook has been set!"
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
