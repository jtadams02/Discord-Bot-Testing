import discord
from discord.ext import commands
import os
# Below will handle getting the discord bot's token to log in
from dotenv import load_dotenv
load_dotenv()
# For testing with bungie stuff 
import aiobungie
# Random number generator
import random
# Bungie API Key a7a359696ab84fcebf7a31bb9b2ebddf
# Probably shouldn't leave that public but whatevs
bclient = aiobungie.Client('a7a359696ab84fcebf7a31bb9b2ebddf')
# Date and Time
from datetime import date
# Discord needs intents to work for some reason
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# I don't know what code below does
# Bot variable?
bot = commands.Bot(command_prefix='$',intents=intents)

@bot.command()
async def whois(ctx):
        await ctx.send("I am a discord bot made in Python by the legendary man JT!")

# Bad words will be placed below
bad_words = ["fuck", "shit", "piss", "bitch", "damn","pussy","jagoff","wanker","cuck","cock","dick"]
# And here will be the responses to the bad words
bad_responses = ["Erm, Language!","That's not gonna fly here buddy","Watch it buster!","I'm warning you kiddo","We don't talk like that around here"]

# Why are these not recognized as variables
daryl = 0
jonah = 0

# Responses to truppa
joe_words = [
    "Not funny",
    "Try again truppa",
    "No one cares",
    "Did anyone ask?"
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(789609064967307274)
    await channel.send("Python Bot Online!")




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$':
        await message.channel.send('$ is my prefix. If you\'d like to see more commands enter "$help"')
        
    if message.content.startswith('$hi'):
        await message.channel.send('Hello there! I am a robot!')
        
    if message.content.startswith('$time'):
        today = date.today()
        await message.channel.send(today)
        return

    # Below code checks whether or not a word in the message matches a word in bad_words    
    if any(word in message.content for word in bad_words): 
        await message.channel.send(random.choice(bad_responses)).then(r => r.delete({ timeout: 5000}))
        return      
        
    # Joe Code
    if message.author.id == 344659595970740226:
        random_number = random.randint(1,5) 
        if random_number == 1: 
            await message.channel.send(random.choice(joe_words))
        return 
    
    # Jonah Code
    if message.author.id == 340542697909518336:
        if jonah == 1:
            jonah = 0
            await message.channel.send("Hello Jonah! I am a Robot!")
        return
        
        
    # JT Code
    #if message.author.id == 173748750068482048:
    #    random_number = random.randint(1,10) 
    #    if random_number == 1: 
    #        await message.channel.send("Random number found!")
    #    return 
        
    if message.author.id == 173748750068482048:
        if jonah == 1:
            jonah = 0
            await message.channel.send("Hi Daryl, I am a robot!")
        return
        
client.run(os.getenv('BOT_TOKEN'))