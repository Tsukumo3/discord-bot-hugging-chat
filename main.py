import pickle
import discord
import os
from flask import Flask, logging
from threading import Thread
from hugchat import hugchat
from hugchat.login import Login

# Flaskで簡単なサーバーを作成
app = Flask(__name__)

# ロガーの設定
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)  # ログレベルを設定
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Hugging Chatのログイン情報
EMAIL = os.getenv("HUGGING_EMAIL")
PASSWD = os.getenv("HUGGING_PASSWORD")
cookie_path_dir = "./cookies/"  # NOTE: trailing slash (/) is required to avoid errors
cookie_file_path = os.path.join(cookie_path_dir, "cookies.pkl")

# クッキーの確認
if os.path.exists(cookie_file_path):
    with open(cookie_file_path, "rb") as f:
        cookies = pickle.load(f)
else:
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    with open(cookie_file_path, "wb") as f:
        pickle.dump(cookies, f)

# ChatBotの作成
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())


# Discord botの設定
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    app.logger.info("ログインしました。")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Userの応答にいいねをする
    emoji = "👍"
    await message.add_reaction(emoji)

    # Hugging Chatを使用してメッセージに応答
    message_result = chatbot.chat(message.content)
    response = message_result.wait_until_done()
    await message.channel.send(response)


@app.route('/')
def home():
    return "Bot is running!"


# サーバーをスレッドで実行
def run_server():
    app.run(host="0.0.0.0", port=8080)


# 環境変数からDiscordトークンを取得
TOKEN = os.getenv("DISCORD_TOKEN")

# サーバーを別スレッドで実行
server_thread = Thread(target=run_server)
server_thread.start()

# Discord botを起動
client.run(TOKEN)
