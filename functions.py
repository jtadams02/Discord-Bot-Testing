# main.py is a little clunky, so I am going to try and separate this and make it cleaner!
import discord
import random

# Function to list all online members
def list_online(message):
    current_channel = message.channel
    member_list = current_channel.members
    
    output = "`The users in `*"
    output+= str(current_channel)
    output+="*` are:\n"
    # Now we have our list of members:
    for member in member_list:
        if member.nick != "None":
            # Create variable to append to output
            toApp = str(member.nick)
            toApp += " and they are currently: "
            toApp += str(member.status)
            
            # Now append the var to the output:
            output+=toApp
            output+='\n'
    output+='`'
    return output
    
    
# Function to list who has sent the most messages in the servers
# Will use a changed version of the above function

async def leaderboard(message):
    # This will hold the server variable
    server = message.channel.guild
    
    # First lets make a list of every user in the server
    user_list = server.members
    
    # Empty list for the corresponding message counts
    msg_counts = []
    
    # Now I want to make a list of all the text channels in the server
    text_channels = server.text_channels
    
    messages = []
    for chunnel in text_channels:
        # Going to need to fetch the message history from each channel
        async for message in chunnel.history():
            if message.author.id != 184405311681986560 and message.author.id != 296023718839451649:
                messages.append(message)
    
    # That should have filled everything up
    for contents in messages:
        print(contents.author.name)
        
    
    
    
# This function is VERY SLOW, going to figure out how to fix it another time?
async def frequency(channel):
    # Pass a channel object as a parameter for the bot. It should be a TextChannel Object
    # It will use this to query all the words from the channel and make a dictionary of them printing the most frequent word!
    
    # Create the empty hashtable?
    words = {}
    async for message in channel.history(limit=None):
        if message.content and message.author.id !=1105708909836128366:
            # This code will only run when the message isn't empty
            # Now we need to loop through all the words of this
            it = 0 
            tempStr = ''
            # So apparently it just makes one big long string instead of a list of strings
            # Idk what I was thinkign so we need to build our own strings from this
            while it < len(message.content):
                if message.content[it] == ' ':
                    # We've hit a space
                    # I want to filter out commands
                    if tempStr.startswith("!") or tempStr.startswith("/") or tempStr.startswith('$'):
                        tempStr = ''
                        continue
                    else:
                        # Now we try to put the word in the dictionary
                        if tempStr in words:
                            words[tempStr] += 1
                        else:
                            words[tempStr] = 1
                        tempStr = ''
                else:
                    tempStr += message.content[it].lower()
                it += 1
        
                
    # That should populate the dictionary with all the things we should need
    
    highestFreq = []
    word = ''
    finalMessage = ''
    for i in range(5):
        freq = 0
        wurd = ''
        for x in words:
            if words[x] > freq:
                freq = words[x]
                wurd = x
        if i == 0: word = wurd
        words.pop(wurd)
        finalMessage += f"{i+1}: {wurd} has been said {freq} times!\n"
        
    embeded = discord.Embed(
        colour=discord.Colour.blue(),
        description=finalMessage,
        title=f"{word}!"
    )
    embeded.set_footer(text="Bleep Bloop - I am a robot!")
    embeded.set_author(name="JT-Bot",url="https://github.com/jtadams02/JT-Bot")
    
    await channel.send(embed=embeded)
            
        
    
    
    
    
