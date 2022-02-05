# Importng discord
import discord
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')


start = False
panda = False

pref = "."
listOfRes = "Please type in any number corresponding to the topic below to learn more about it!\n\n(1) Extinction of red pandas\n(2) Saving the ocean\n(3) Pandemic affecting our daily lives\n(4) Story behind black history month\n(5) Muslim persecution in China\n(6) Gun violence in America\n(7) Our carbon footprint\n(8) Saving the Amazon Rainforest\n(9) Global warming\n(10) Wildlife loss and their factors"
topicmessage = " Below is a list of choices you can choose to learn more about this topic:"
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
    global start
    global panda
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
        start = True
        return

    # Red Pandas
    if start and msg == "1":
        await message.channel.send("Nice to know you have an interest in red pandas!"+topicmessage)
        await message.channel.send("(1) What are red pandas?")
        await message.channel.send("(2) How and why are they endangered?")
        await message.channel.send("(3) How can you help?")
        await message.channel.send("(4)Why should you care?")
        panda = True
        start = False
        return

    if panda and msg == "1":
        await message.channel.send("The red panda, sometimes known as the smaller panda, is a carnivorous creature that can be found in the eastern Himalayas and southwestern China. It features a ringed tail, dense reddish-brown fur, white-lined ears, and a largely white nose. It has a head-to-body length of 510–635 mm and a tail length of 280–485 mm. It is between 3.2 and 15 kg in weight.")
        return


    if msg == ".end":
        await message.channel.send('Thank you for using Learn it All! Hope you learned something new today.')
        quit()

# client.run(botTKN)
client.run(os.getenv('tkn'))