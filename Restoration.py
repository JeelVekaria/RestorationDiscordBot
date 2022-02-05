# Importng discord
import discord
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')


start = False
panda = False
repeat = False
repeatPanda = False
ron = "\n\n**Would you like to:**\n:one: Continue learning more about this topic\n:two: Move onto another topic"

pref = "."
listOfRes = "**Please type in any number corresponding to the topic below to learn more about it!**\n\n:one: Extinction of red pandas\n:two: Saving the ocean\n:three: Pandemic affecting our daily lives\n:four: Story behind black history month\n:five: Muslim persecution in China\n:six: Gun violence in America\n:seven: Our carbon footprint\n:eight: Saving the Amazon Rainforest\n:nine: Global warming\n:keycap_ten: Wildlife loss and their factors"
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
    global repeat
    global repeatPanda
    messaged = str(message.content)
    msg = messaged.lower()
    send = message.channel.send

    if message.author == client.user:
        return

    if msg == pref+"status":
        await send("I'm up and running! Please type \".summon\" to begin this session!")
        return

    if msg == pref+"testing":
        print("It works!")
        await send("yep I'm working")
        return

    if msg == pref+"quote":
        await send(get_quote())
        return

    # Main part of the project
    if msg == pref+"summon":
        await send(listOfRes)
        start = True
        return

    # Red Pandas
    if repeat and panda and msg == "1":
        start = True
        repeat = False
    if repeat and panda and msg == "2":
        panda = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "1":
        await send("**Nice to know you have an interest in red pandas!"+topicmessage+"**\n:one: What are red pandas?\n:two: How and why are they endangered?\n:three: How can you help?\n:four: Why should you care?")
        panda = True
        start = False
        return

    if panda and msg == "1" and repeat == False:
        await send("The red panda, sometimes known as the smaller panda, is a carnivorous creature that can be found in the eastern Himalayas and southwestern China. It features a ringed tail, dense reddish-brown fur, white-lined ears, and a largely white nose. It has a head-to-body length of 510–635 mm and a tail length of 280–485 mm. It is between 3.2 and 15 kg in weight."+ron)
        repeat = True
        return

    if panda and msg == "2" and repeat == False:
        await send("Habitat loss and degradation, human meddling, and poaching are the main dangers they face. The total number of red pandas is thought to have decreased by 40% in the last two decades, according to researchers."+ron)
        repeat = True
        return

    if panda and msg == "3" and repeat == False:
        await send("Spreading awareness, donating and fundraising, participating in ecotourism, and working against the red panda trade are all ways to become engaged."+ron)
        repeat = True
        return

    if panda and msg == "4" and repeat == False:
        await send("Protecting their habitats saves other threatened creatures such as Himalayan black bears, clouded leopards, and numerous bird species. They help balance the ecosystem. They are the “umbrella species” of the Himalayan region."+ron)
        repeat = True
        return

    # Saving the Ocean
    # if start and msg == "2":
    #     await send("**Good to see others who are interested in saving our oceans!"+topicmessage+"**\n:one: What’s happening to our oceans?\n:two: Why care about marine life and the ocean in general?\n:three: How can you stop contributing to this disaster?\n:four: How to support more?")
    #     panda = True
    #     start = False
    #     return
    








    if msg == ".end":
        await send('Thank you for using Learn it All! Hope you learned something new today.')
        quit()

# client.run(botTKN)
client.run(os.getenv('tkn'))