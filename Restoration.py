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
forest = False
china = False
carbon = False
america = False
normal = False
warming = False
wildlife = False

repeat = False
ron = "\n\n**Would you like to:**\n:one: Continue learning more about this topic\n:two: Move onto another topic"

pref = "."
listOfRes = "**Please type in any number corresponding to the topic below to learn more about it!**\n\n:one: Extinction of Red Pandas\n:two: Saving our Ocean\n:three: Promoting Black History Month \n:four: Saving the Amazon Rainforest\n:five: Uyghurs Persecution in China\n:six: Gun Violence in America\n:seven: Our Carbon Footprint\n:eight: Pandemic Affecting our Daily Lives\n:nine: Global warming\n:keycap_ten: Wildlife Loss and their Factors"
topicmessage = " Below is a list of choices you can choose to learn more about this topic:"
# Discord Client
client = discord.Client()

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
    global forest
    global china
    global america
    global carbon
    global normal
    global warming
    global wildlife
    global repeat
    messaged = str(message.content)
    msg = messaged.lower()
    send = message.channel.send

    if msg == ".end":
        await send('Thank you for using Learn it All! Hope you learned something new today.')
        quit()

    if msg == ".cls":
        for i in range(4):
            await send(file=discord.File('clear.png'))
        return
    if message.author == client.user:
        return

    if msg == pref+"status":
        await send("I'm up and running! Please type \".summon\" to begin this session!")
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
        await send("**Nice to know you have an interest in red pandas!"+topicmessage+"**\n:one: What are red pandas?\n:two: How and why are they endangered?\n:three: How can we help?\n:four: Why should we care?")
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
        await send("**Good to see others who are interested in saving our oceans!"+topicmessage+"**\n:one: What’s happening to our oceans?\n:two: Why care about marine life and the ocean in general?\n:three: How can we stop contributing to this disaster?\n:four: How to support more?")
        ocean = True
        start = False
        return
    
    if ocean and msg == "1" and repeat == False:
        await send("Sea levels are rising as a result of global warming, posing a hazard to coastal population areas. Many agricultural chemicals and nutrients end up in coastal waterways, causing oxygen depletion and the death of marine plants and crustaceans. Sewage and other runoff from factories and industrial plants are discharged into the oceans. Below is a useful link to explain more about this:\nhttps://www.nationalgeographic.com/environment/article/ocean-threats#:~:text=Global%20warming%20is%20causing%20sea,other%20runoff%20into%20the%20oceans. "+ron)
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
        await send("Overall try to reduce your carbon footprint and support local or well known organizations that are fighting these issues or similar issues, such as teamseas https://teamseas.org/"+ron)
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

    # Amazon rainforest
    if repeat and forest and msg == "1":
        start = True
        repeat = False
        forest = False
    if repeat and forest and msg == "2":
        forest = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "4" or start and msg == "1" and not forest:
        await send("**Yay this is a nice topic! Let's learn more about the Amazon Rainforest!"+topicmessage+"**\n:one: What’s the issue with Amazon Forest?\n:two: How is the area impacted and its significance?\n:three: Why should we care?\n:four: How can we help?")
        forest = True
        start = False
        return
    
    if forest and msg == "1" and repeat == False:
        await send("Deforestation. Deforestation is one of the most serious and well-known issues in the Amazon. While trees have been taken down for logging, industrialization, and human expansion, farming is responsible for the most intense and dramatic deforestation in the Amazon rainforest.  "+ron)
        repeat = True
        return
    if forest and msg == "2" and repeat == False:
        await send(" Growing temperatures and altering rain patterns in the Amazon will almost certainly result from global climate change and increased deforestation over time, affecting the region's forests, water availability, biodiversity, agriculture, and human health. "+ron)
        repeat = True
        return
    if forest and msg == "3" and repeat == False:
        await send(" The Amazon rainforest is crucial in managing the global oxygen and carbon cycles. It produces about 6% of the world's oxygen and has long been assumed to operate as a carbon sink, absorbing enormous amounts of carbon dioxide from the atmosphere quickly. "+ron)
        repeat = True
        return
    if forest and msg == "4" and repeat == False:
        await send("Support by donating to https://www.wwf.org.uk/where-we-work/amazon and other organizations. Cut down on the use of paper and save our trees! Reduce oil and beef consumption, oil is a pollutant in the environment and cows produce methane which is another pollutant in our environment, plus they need grasslands to feed on meaning more deforestation.. Invest more into rainforest communities! "+ron)
        repeat = True
        return

    # Uyghurs Persecution in China 
    if repeat and china and msg == "1":
        start = True
        repeat = False
        china = False
    if repeat and china and msg == "2":
        china = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "5" or start and msg == "1" and not china:
        await send("**Good topic to be knowledgable about!"+topicmessage+"**\n:one: Who are they?\n:two: How many people are being affected?\n:three: Why bother?\n:four: How to support victims?")
        china = True
        start = False
        return
    
    if china and msg == "1" and repeat == False:
        await send("Xinjiang, formally known as the Xinjiang Uyghur Autonomous Region, is home to over 12 million Uyghurs, the majority of whom are Muslim (XUAR). The Uyghurs speak a language that is akin to Turkish and consider themselves to be culturally and ethnically related to Central Asian countries. They make up less than half of the population of Xinjiang. https://www.bbc.com/news/world-asia-china-22278037 "+ron)
        repeat = True
        return
    if china and msg == "2" and repeat == False:
        await send(" 12 million and counting more because its Muslims in general too. It’s an ongoing genocide in the “internment camps”"+ron)
        repeat = True
        return
    if china and msg == "3" and repeat == False:
        await send(" This is against human rights! It shouldn’t be happening to anyone.  "+ron)
        repeat = True
        return
    if china and msg == "4" and repeat == False:
        await send(" Speak up for them, spread awareness on social media. Donate to relief organisations. https://icnareliefcanada.ca/uyghur-relief "+ron)
        repeat = True
        return


    # What’s happening with arms in the U.S?
    if repeat and america and msg == "1":
        start = True
        repeat = False
        america = False
    if repeat and america and msg == "2":
        america = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "6" or start and msg == "1" and not america:
        await send("**This is a good topic that you should know about!"+topicmessage+"**\n:one: What’s happening with arms in the U.S?\n:two: Who is impacted? \n:three: Why care?\n:four: How to support victims?")
        america = True
        start = False
        return
    
    if america and msg == "1" and repeat == False:
        await send("Xinjiang, formally known as the Xinjiang Uyghur Autonomous Region, is home to over 12 million Uyghurs, the majority of whom are Muslim (XUAR). The Uyghurs speak a language that is akin to Turkish and consider themselves to be culturally and ethnically related to Central Asian countries. They make up less than half of the population of Xinjiang. https://www.bbc.com/news/world-asia-china-22278037 "+ron)
        repeat = True
        return
    if america and msg == "2" and repeat == False:
        await send(" 12 million and counting more because its Muslims in general too. It’s an ongoing genocide in the “internment camps”"+ron)
        repeat = True
        return
    if america and msg == "3" and repeat == False:
        await send(" This is against human rights! It shouldn’t be happening to anyone.  "+ron)
        repeat = True
        return
    if america and msg == "4" and repeat == False:
        await send("How to support victims? Spread awareness on the Internet and donate to American hospitals or gather people for protests. http://gvsfoundation.org/"+ron)
        repeat = True
        return



    # Our Carbon Footprint
    if repeat and carbon and msg == "1":
        start = True
        repeat = False
        carbon = False
    if repeat and carbon and msg == "2":
        carbon = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "7" or start and msg == "1" and not carbon:
        await send("**This is a good topic that you should know about!"+topicmessage+"**\n:one:What in the world is that?\n:two: Why should we care? \n:three: How to make a difference?")
        carbon = True
        start = False
        return
    
    if carbon and msg == "1" and repeat == False:
        await send("The total amount of greenhouse gases (including carbon dioxide and methane) produced by our actions is referred to as our carbon footprint. By 2050, the average worldwide carbon footprint per year must be under 2 tonnes to have the best chance of averting a 2°C rise in global temperatures. https://www.nature.org/en-us/get-involved/how-to-help/carbon-footprint-calculator/#:~:text=A%20carbon%20footprint%20is%20the,are%20generated%20by%20our%20actions.&text=To%20have%20the%20best%20chance,under%202%20tons%20by%202050. "+ron)
        repeat = True
        return
    if carbon and msg == "2" and repeat == False:
        await send("The planet's resources are consumed in various amounts by the world's seven billion people. According to UN estimates, the global population will reach 9.7 billion by 2050, and more than 11 billion by 2100. Population growth increases emissions and DEPLETES THE PLANET’S RESOURCES! "+ron)
        repeat = True
        return
    if carbon and msg == "3" and repeat == False:
        await send("Global warming is intensified by increased greenhouse gas emissions. It hastens climate change, which has severe consequences for our world. By making climate-friendly decisions in our daily lives, we can all help to combat global warming. Such decisions include not using automobiles for simple tasks that can be accomplished by walking or biking and using cloth bags instead of plastic ones in grocery stores. https://europa.eu/youth/get-involved/sustainable-development/how-reduce-my-carbon-footprint_en "+ron)
        repeat = True
        return

    # Normal Life (Pre-COVID)
    if repeat and normal and msg == "1":
        start = True
        repeat = False
        normal = False
    if repeat and normal and msg == "2":
        normal = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "8" or start and msg == "1" and not normal:
        await send("**This is a good topic that you should know about!"+topicmessage+"**\n:one:What it used to be like before COVID-19 came along?\n:two: How much has this virus affected the world? \n:three: What can we do to stop it’s mutation?\n:four: Why bother caring?")
        normal = True
        start = False
        return
    
    if normal and msg == "1" and repeat == False:
        await send("Life was normal and we didn’t have an annoying piece of cloth on our faces which we call the masks. Students used to go and learn inside a school building not through an online web conference tool such as Google Meet or Zoom. We all had to sit in our homes and quarantine as well which I’m pretty sure was boring for most of us. "+ron)
        repeat = True
        return
    if normal and msg == "2" and repeat == False:
        await send(" This virus has killed 5.73 million people worldwide and numerous economies have crashed, small businesses are having a tough time managing with all the covid restrictions. People are experiencing a lot of anxiety and stress, meaning MENTAL HEALTH IS BEING AFFECTED! "+ron)
        repeat = True
        return
    if normal and msg == "3" and repeat == False:
        await send("We can continue social distance, wearing our masks and sanitizing more often. In cases of possible COVID symptoms we must stay home, take care of ourselves, and keep in mind the safety of others. BE UP TO DATE WITH VACCINES! Vaccines are our strongest weapon against this virus after self isolation."+ron)
        repeat = True
        return
    if normal and msg == "4" and repeat == False:
        await send("We should care because we want more social interactions, no more masks and freedom from all these restrictions put in place to prevent this virus. Most importantly we must care because people's lives are at stake. You could also donate to hospitals and food banks and make a difference for people who are facing a tremendous amount of stress coping with COVID due to the financial crisis. https://www.frontlinefund.ca/ and https://www.foodbankscanada.ca/COVID-19.aspx "+ron)
        repeat = True
        return


    # Global Warming
    if repeat and warming and msg == "1":
        start = True
        repeat = False
        warming = False
    if repeat and warming and msg == "2":
        warming = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "9" or start and msg == "1" and not warming:
        await send("**This is a good topic that you should know about!"+topicmessage+"**\n:one:What is it?\n:two: How is it affecting the world?\n:three: How is it related to other crises? \n:four: What can we do to prevent it? ")
        warming = True
        start = False
        return
    
    if warming and msg == "1" and repeat == False:
        await send("The term \"global warming\" refers to the increase in the global average temperature. It has to deal with the Earth's overall climate, not the weather on any individual day. https://www.ducksters.com/science/environment/global_warming.php "+ron)
        repeat = True
        return
    if warming and msg == "2" and repeat == False:
        await send("Storms, heat waves, floods, and droughts are all worsening as a result of rising temperatures. A warmer temperature produces an atmosphere that can gather, hold, and drop more water, altering weather patterns such that wet areas grow wetter and dry ones become drier. https://www.nrdc.org/stories/are-effects-global-warming-really-bad#:~:text=More%20frequent%20and%20severe%20weather,wetter%20and%20dry%20areas%20drier. "+ron)
        repeat = True
        return
    if warming and msg == "3" and repeat == False:
        await send("Climate change intensifies competition for resources such as land, food, and water, escalating social conflicts and, increasingly, resulting in mass relocation. Climate change is a risk multiplier, worsening existing problems. https://www.un.org/en/un75/climate-crisis-race-we-can-win#:~:text=The%20effects%20of%20climate%20change,makes%20worse%20already%20existing%20challenges. "+ron)
        repeat = True
        return
    if warming and msg == "4" and repeat == False:
        await send("Power our homes with renewable energy, buy longer lasting light bulbs, go on a vegan diet (meat plays a major role in the contribution of climate change - see topics above), or invest in energy efficient appliances. There are even more ways to make a difference from your end like donate or start a fundraiser and even spread the word on social media! https://www.canadahelps.org/en/donate-to-environmental-charities-giving-back-to-the-planet/  and https://www.theatlantic.com/science/archive/2020/12/how-to-donate-to-fight-climate-change-effectively/617248/ "+ron)
        repeat = True
        return

    # Wildlife Loss
    if repeat and wildlife and msg == "1":
        start = True
        repeat = False
        wildlife = False
    if repeat and wildlife and msg == "2":
        wildlife = False
        await send(listOfRes)
        start = True
        repeat = False
        return

    if start and msg == "10" or start and msg == "1" and not wildlife:
        await send("**This is a good topic that you should know about!"+topicmessage+"**\n:one:What’s the reason of wildlife loss?\n:two: How is earth affected?\n:three: Why should we care? \n:four: How can we support the animals? ")
        wildlife = True
        start = False
        return
    
    if wildlife and msg == "1" and repeat == False:
        await send("The biggest hazard to wildlife survival in the United States is habitat loss, which occurs as a result of habitat destruction, fragmentation, or degradation. When an ecosystem is drastically altered by human activities like agriculture, oil and gas exploration, commercial development, or water diversion, it may no longer be able to offer the food, water, cover, and places to raise young that species require to thrive. Every day, animals have fewer and fewer places to call home. https://www.nwf.org/Educational-Resources/Wildlife-Guide/Threats-to-Wildlife/Habitat-Loss "+ron)
        repeat = True
        return
    if wildlife and msg == "2" and repeat == False:
        await send("What are the ramifications of a species' extinction? If a species serves a particular purpose in its ecosystem, its extinction can have cascading repercussions down the food chain (a \"trophic cascade\"), affecting other species as well as the ecosystem as a whole. https://news.climate.columbia.edu/2019/03/26/endangered-species-matter/ "+ron)
        repeat = True
        return
    if wildlife and msg == "3" and repeat == False:
        await send("When a wild animal's natural habitat is destroyed, the animals will flee to the human environment. There will be no more room for animals, and they will be forced to die. Plants, on the other hand, will grow massively, disrupting the entire life cycle and feeding cycle. https://goprep.co/what-will-happen-if-the-natural-habitat-of-a-wild-animal-is-i-1njjg3 "+ron)
        repeat = True
        return
    if wildlife and msg == "4" and repeat == False:
        await send("Volunteer or donate to an animal shelter. Start a fundraiser for endangered animals see topic 1 as an example (Hint: Red Pandas). \nDonate to an animal welfare organisation. \nhttps://www.petsafe.net/learn/how-to-help-animals-in-your-community.\nLink to donate for animals https://www.canadahelps.org/en/explore/charities/category/animals/ \nhttps://ontariospca.ca/how-to-help/other-ways-to-donate/"+ron)
        repeat = True
        return



client.run(os.getenv('tkn'))