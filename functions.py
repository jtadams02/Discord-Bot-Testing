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
    
    
# Helper function for puring bot messages
def is_me(m):
    return m.author == client.user