from flask import Flask
import logging

# Flaskで簡単なサーバーを作成
app = Flask(__name__)

# Flaskのロガーの設定
flask_logger = logging.getLogger("werkzeug")
flask_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
flask_logger.addHandler(handler)


@app.route("/")
def home():
    return "Bot is running!"


def run_server():
    app.run(host="0.0.0.0", port=8080)
