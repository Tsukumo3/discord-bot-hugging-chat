import logging
import discord
import os
from dotenv import load_dotenv


load_dotenv()

# Discordボットのロガーの設定
logging.basicConfig(level=logging.DEBUG)  # DEBUGレベルに設定
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)

# Discord botの設定
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # メッセージの内容を取得するためのIntent
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    logger.info("ログインしました。")


@client.event
async def on_message(message):
    logger.info(f"メッセージを受信: {message.content} from {message.author}")

    if message.author == client.user:
        return

    # Userの応答にいいねをする
    emoji = "👍"
    await message.add_reaction(emoji)

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == "/neko":
        await message.channel.send("にゃーん")


def run_bot():
    TOKEN = os.getenv("DISCORD_TOKEN")
    client.run(TOKEN)
