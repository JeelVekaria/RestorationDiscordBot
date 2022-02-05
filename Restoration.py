# Importng discord
import discord
import json
import os
from dotenv import load_dotenv
load_dotenv('.env')



# Discord Client
client = discord.Client()


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

# client.run(botTKN)
client.run(os.getenv('tkn'))