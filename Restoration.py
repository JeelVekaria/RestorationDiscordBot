# Importng discord
import discord
import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    config = {"Token":""}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(config, f)

botTKN = configData["Token"]

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

client.run(botTKN)