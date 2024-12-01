import discord
import os
from flask import Flask
from threading import Thread

# Discord botの設定
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    emoji = "👍"
    await message.add_reaction(emoji)

# Flaskで簡単なサーバーを作成
app = Flask(__name__)


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
