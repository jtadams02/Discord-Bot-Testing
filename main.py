import discord
import os

from datetime import date

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Bad words will be placed below
bad_words = ["fuck", "shit", "piss", "bitch", "damn"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello there! I am a robot!')
        
    if message.content.startswith('$time'):
        today = date.today()
        await message.channel.send(today)
        
    if any(word in message.content for word in bad_words): 
        await message.channel.send("Erm, language!")
        
    if message.author.id == 344659595970740226:
        await message.channel.send("I am sorry, but your meme is not funny Joe")
        
client.run('MTEwNTcwODkwOTgzNjEyODM2Ng.GfcnBr.d_xsQInizoxhM8_HnL71ebq_RCVHtZa6GI3rRA')