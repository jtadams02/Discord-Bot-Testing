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
            messages.append(message)
    
    # That should have filled everything up
    for contents in messages:
        print(contents.author.name)
        
        
    