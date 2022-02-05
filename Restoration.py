# Importng discord
import discord

# Discord Client
client = discord.Client()

# Discord bot Token
botTKN = "OTM5MzY3NTEwNDg5MzE3Mzc3.Yf30Kw.hF_AzA_26ayhf6i2lwoN9bJt55I"

@client.event
async def on_ready():
    print("Bot is now active!")

@client.event
async def on_message(message):
    messaged = str(message.content)

    if message.author == client.user:
        return

    if messaged.lower() == "testing":
        print("It works!")

client.run(botTKN)