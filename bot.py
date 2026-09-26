import os
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

SOURCE_CHANNEL_ID = 123456789012345678  # Thay bằng ID kênh gốc
TARGET_CHANNEL_ID = 987654321098765432  # Thay bằng ID kênh đích

@client.event
async def on_ready():
    print(f"Bot đã online: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == SOURCE_CHANNEL_ID:
        target_channel = client.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            content = f"**{message.author.display_name}:** {message.content}"
            files = [await a.to_file() for a in message.attachments]
            await target_channel.send(content=content, files=files)

# Lấy token từ Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
