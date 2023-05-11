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
import datetime,time
# UserList

# We need our list of no-no words, lets get it
bad_words = []
f = open('swearlist.txt','r+')
for line in f:
    bad_words.append(line.strip().lower())
# And here will be the responses to the bad words
bad_responses = ["Erm, Language!","That's not gonna fly here buddy","Watch it buster!","I'm warning you kiddo","We don't talk like that around here"]
# And here will be the responses to the people who are excluded
in_the_clear = ["I didn't see anything","I'll let it slide this time","She gets a pass","I'm misandrist so I'll just ignore this"]
# Responses to truppa
joe_words = [
    "Not funny",
    "Try again truppa",
    "No one cares",
    "Did anyone ask?"
]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# Time that the discord client starts????
startTime = time.time()
# I don't know what code below does
# Bot variable?

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.command()
async def whois(ctx):
        await ctx.send("I am a discord bot made in Python by the legendary man JT!")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(789609064967307274)
    startTime = time.time()
    # await channel.send("Raspberry Py Online!")




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # This is just the prefix command. I know I'm not doing commands right but I'm learning okay
    if message.content == '$':
        await message.channel.send("`$ is my prefix. If you\'d like to see more commands enter \"$help\"\nI am a bot coded in Python by JT`")
        return

    # Simple help command
    if message.content == '$help':
        await message.channel.send("`There aren't a lot of commands right now, but here's what we got:\n$swear : Report a swear word you would like to add to the no-no list`")
        return

    # Ideally this will add the given swear to the swear list. Jt should maintain the swear list to make sure it is right
    if message.content.startswith("$swear"):
        msg = message.content
        if len(msg.split()) < 2:
            await message.reply("We're sorry, but we cannot add an empty space to the list",delete_after=5.0)
            return
        swear = msg.split(' ')[1]
        if swear.isspace():
            await message.reply("We're sorry, but we cannot add an empty space to the list",delete_after=5.0)
            return
        temp = f # Temp variable I do not think is needed!
        if swear.lower() in bad_words:
            await message.reply("We're sorry, but that swear is already on the list!",delete_after=5.0)
            return
        else:
            temp.write('\n'+swear.lower())
            bad_words.append(swear.lower())
            toSend = (swear+' has been added to the swearlist. Thank you for making our server a safer place!')
            await message.channel.send(toSend)
            return

    if message.content == '$uptime':
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        msg = 'JT Bot has been active for: ' + str(uptime)
        await message.channel.send(msg)
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello there! I am a robot!')

    if message.content.startswith('$time'):
        today = datetime.today()
        await message.channel.send(today)
        return

    # Below code checks whether or not a word in the message matches a word in bad_words
    # delete_after causes the message to delete after 5 seconds!
    if any(word in message.content.lower() for word in bad_words):
            if message.author.id == 743721232326852628:
                await message.reply(random.choice(in_the_clear),delete_after=5.0)
                return
            else:
                await message.reply(random.choice(bad_responses),delete_after=5.0)
                return
    # Joe Code, just respondes to joe lol
    if message.author.id == 344659595970740226:
        random_number = random.randint(1,5)
        if random_number == 1:
            await message.reply(random.choice(joe_words,delete_after=5.0))
        return

client.run(os.getenv('BOT_TOKEN'))
