import discord
from discord.ext import commands

import os
# For testing with bungie stuff 
import aiobungie
import random

# Bungie API Key a7a359696ab84fcebf7a31bb9b2ebddf
# Probably shouldn't leave that public but whatevs
bclient = aiobungie.Client('a7a359696ab84fcebf7a31bb9b2ebddf')


from datetime import date

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Bot variable?
bot = commands.Bot(command_prefix='$',intents=intents)

@bot.command()
async def whois(ctx):
        await ctx.send("I am a discord bot made in Python by the legendary man JT!")

# Bad words will be placed below
bad_words = ["fuck", "shit", "piss", "bitch", "damn"]

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello there! I am a robot!')
        
    if message.content.startswith('$hi'):
        await message.channel.send('Hello there! I am a robot!')
        
    if message.content.startswith('$time'):
        today = date.today()
        await message.channel.send(today)
        return
        
    if any(word in message.content for word in bad_words): 
        await message.channel.send("Erm, language!")
        return
        
    # Joe Code
    if message.author.id == 344659595970740226:
        random_number = random.randint(1,5) 
        if random_number == 1: 
            await message.channel.send(random.choice(joe_words))
        return 
        
    # JT Code
    #if message.author.id == 173748750068482048:
    #    random_number = random.randint(1,10) 
    #    if random_number == 1: 
    #        await message.channel.send("Random number found!")
    #    return 
        
    if message.author.id == 447520381218193408:
        await message.channel.send("Hi daryl")
        
client.run('MTEwNTcwODkwOTgzNjEyODM2Ng.GfcnBr.d_xsQInizoxhM8_HnL71ebq_RCVHtZa6GI3rRA')