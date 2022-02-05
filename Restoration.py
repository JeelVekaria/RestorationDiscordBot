# Importng discord
import discord
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')


start = False
panda = False
ocean = False
black = False






repeat = False
ron = "\n\n**Would you like to:**\n:one: Continue learning more about this topic\n:two: Move onto another topic"

pref = "."
listOfRes = "**Please type in any number corresponding to the topic below to learn more about it!**\n\n:one: Extinction of red pandas\n:two: Saving the ocean\n:three: Story behind black history month \n:four: Pandemic affecting our daily lives\n:five: Muslim persecution in China\n:six: Gun violence in America\n:seven: Our carbon footprint\n:eight: Saving the Amazon Rainforest\n:nine: Global warming\n:keycap_ten: Wildlife loss and their factors"
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
    global ocean
    global black
    global repeat
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
        panda = False
    if repeat and panda and msg == "2":
        panda = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "1" or start and msg=="1" and not panda:
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
        await send("Spreading awareness, donating and fundraising, participating in ecotourism, and working against the red panda trade are all ways to become engaged. A website that you can contribute to https://redpandanetwork.org/ "+ron)
        repeat = True
        return

    if panda and msg == "4" and repeat == False:
        await send("Protecting their habitats saves other threatened creatures such as Himalayan black bears, clouded leopards, and numerous bird species. They help balance the ecosystem. They are the “umbrella species” of the Himalayan region."+ron)
        repeat = True
        return

    # Saving the Ocean
    if repeat and ocean and msg == "1":
        start = True
        repeat = False
        ocean = False
    if repeat and ocean and msg == "2":
        ocean = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "2" or start and msg == "1" and not ocean:
        await send("**Good to see others who are interested in saving our oceans!"+topicmessage+"**\n:one: What’s happening to our oceans?\n:two: Why care about marine life and the ocean in general?\n:three: How can you stop contributing to this disaster?\n:four: How to support more?")
        ocean = True
        start = False
        return
    
    if ocean and msg == "1" and repeat == False:
        await send("Sea levels are rising as a result of global warming, posing a hazard to coastal population areas. Many agricultural chemicals and nutrients end up in coastal waterways, causing oxygen depletion and the death of marine plants and crustaceans. Sewage and other runoff from factories and industrial plants are discharged into the oceans."+ron)
        repeat = True
        return
    if ocean and msg == "2" and repeat == False:
        await send("The oxygen we breathe is produced by the ocean, which absorbs 50 times more carbon dioxide than our atmosphere. The ocean, which covers 70% of the Earth's surface and transfers heat from the equator to the poles, regulates our temperature and weather patterns by transporting heat from the equator to the poles. "+ron)
        repeat = True
        return
    if ocean and msg == "3" and repeat == False:
        await send(" Try to avoid use of vehicles for simple tasks. Conserve energy and water, like turning the tap off while brushing your teeth or not taking extra long showers. Stop the use of plastic items. Don’t purchase endangered fish or seafood."+ron)
        repeat = True
        return
    if ocean and msg == "4" and repeat == False:
        await send("Overall try to reduce your carbon footprint and support teamseas https://teamseas.org/ and support WWF for marine conservation https://www.worldwildlife.org/initiatives/oceans"+ron)
        repeat = True
        return


    # Black History Month
    if repeat and black and msg == "1":
        start = True
        repeat = False
        black = False
    if repeat and black and msg == "2":
        black = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "3" or start and msg == "1" and not black:
        await send("**Nice to see you are interested in the story of black history month!"+topicmessage+"**\n:one: What has happened to Black People?\n:two: What’s the current situation for them?\n:three: How to support and restore their racial justice?")
        black = True
        start = False
        return
    
    if black and msg == "1" and repeat == False:
        await send("Black people had been enslaved in the 1600s by Europeans and then shipped to America to work on plantations. The rural South, where slavery had gained the strongest hold in North America, suffered an economic crisis in the years following the Revolutionary War. Tobacco, the most profitable cash crop at the time, had depleted the soil, while rice and indigo failed to yield much profit. As a result, the cost of enslaved individuals was falling, and the future of slavery appeared to be in doubt. "+ron)
        repeat = True
        return
    if black and msg == "2" and repeat == False:
        await send("The visceral public display of George Floyd’s murder and COVID-19 had engulfed the U.S in a manner markedly distinct from Ferguson, Black Lives Matter (BLM) and other previous nation-wide racial justice movements. At the same time, with the world and the mainstream media gripped by the pandemic's sweeping halt, BLM took to social media, releasing raw footage of Floyd and other Black victims to show that they were not isolated incidents, but rather the remnants of a larger scourge of racially charged police violence sweeping the country.  "+ron)
        repeat = True
        return
    if black and msg == "3" and repeat == False:
        await send("Visit a Black or African American history museum, support black businesses. Most importantly, donate to Black organisations and charities such as https://secure.actblue.com/donate/ms_blm_homepage_2019 https://www.tmcf.org/online-gift/  and http://www.blackgirlscode.com/donate/"+ron)
        repeat = True
        return
    if black and msg == "4" and repeat == False:
        await send("Overall try to reduce your carbon footprint and support teamseas https://teamseas.org/ and support WWF for marine conservation https://www.worldwildlife.org/initiatives/oceans"+ron)
        repeat = True
        return












    if msg == ".end":
        await send('Thank you for using Learn it All! Hope you learned something new today.')
        quit()

# client.run(botTKN)
client.run(os.getenv('tkn'))