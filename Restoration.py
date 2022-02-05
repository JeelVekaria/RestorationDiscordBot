# Importng discord
import discord
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')

pref = "."
listOfRes = "Please type in any number corresponding to the topic below to learn more about it!\n\n(1) Extinction of red pandas\n(2) Saving the ocean\n(3) Pandemic affecting our daily lives\n(4) Story behind black history month\n(5) Muslim persecution in China\n(6) Gun violence in America\n(7) Our carbon footprint\n(8) Saving the Amazon Rainforest\n(9) Global warming\n(10) Wildlife loss and their factors"
# Discord Client
client = discord.Client()


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -"+json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print("Bot is now active!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='YOUR REQUESTS :)'))


@client.event
async def on_message(message):
    messaged = str(message.content)
    msg = messaged.lower()

    if message.author == client.user:
        return

    if msg == pref+"status":
        await message.channel.send("I'm up and running! Please type \".summon\" to begin this session!")
        return

    if msg == pref+"testing":
        print("It works!")
        await message.channel.send("yep I'm working")
        return

    if msg == pref+"quote":
        await message.channel.send(get_quote())
        return

    # Main part of the project
    if msg == pref+"summon":
        await message.channel.send(listOfRes)



    if msg == ".end":
        await message.channel.send('Thank you for using Learn it All! Hope you learned something new today.')
        quit()

# client.run(botTKN)
client.run(os.getenv('tkn'))