from flask import Flask, request, jsonify, render_template
import telegram
import os

# Fetch Telegram Bot Token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_USERNAME = "orewapp_bot"

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/webapp", methods=["POST"])
def webapp_data():
    data = request.json
    print("Received from WebApp:", data)
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
