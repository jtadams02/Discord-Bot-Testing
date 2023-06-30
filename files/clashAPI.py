# Learning how API's work!
import requests
import json

# Im going to import discord to make embeds
import discord

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    print(text)

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkN2Y2ZDFlLWVjNjktNGJkOS1iNjQ3LTFhM2U2OTFhZGI2OCIsImlhdCI6MTY4NzkwOTkzMSwic3ViIjoiZGV2ZWxvcGVyLzlkYjBiY2Q3LTU4MjAtNmRlMS1iOGNlLTQ1OWM4NDEwNGMxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNC4xNC4yNDcuMTczIl0sInR5cGUiOiJjbGllbnQifV19.3_NJmRz_o6AuhWJErW8ASjw0ARSQugzjZAwby8Sy0iZoEPkCxnIiJMePg0BuRuPAPE5NF60vt83jgduqeL89NA"
LAPTOP_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRlOTQzZDFkLTgwMGYtNGFmNi1iN2M4LTYwNmJkMjAxZjRhYiIsImlhdCI6MTY4ODE0MjE4NCwic3ViIjoiZGV2ZWxvcGVyLzlkYjBiY2Q3LTU4MjAtNmRlMS1iOGNlLTQ1OWM4NDEwNGMxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzIuNTguMTY1LjE2MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.o9w2GByOkPfTQ0lxMBLR0Dp9ZOE8FDjbB_WmWP4Z8ugbzZMuXLEo898nPMjng0er9Ve3aBod6zwQn6WczPXvnQ"
# Lets Test it out

BASE_URL = "https://api.clashroyale.com/v1/"

PLAYERS = "players/%23"

t = '8VGUUC0J'
h = {'Authorization' : 'Bearer {}'.format(LAPTOP_KEY)}

def player_lookup(tag):
    print(tag)
    return_embed = discord.Embed() # Initialize Object
    api = requests.get(BASE_URL+PLAYERS+tag,headers=h)
    if api.status_code == 200:
        api = api.json()
        # return_embed.set_thumbnail(url=api['currentFavouriteCard']['iconUrls']['medium'])
        return_embed.title = f"ClashAPI Statistics"
        return_embed.description = f"""\"*This bot is a major work in progress*\"
        Account: **{api['name']} {api['tag']}**
        Clan: **{api['clan']['name']} {api['clan']['tag']}**
        Trophies: **{api['trophies']}**
        Upcoming Chests
        """
        return_embed.set_footer(text="Bleep Bloop - Coded by JT")
        return return_embed
    else:
        return 0

BATTLES = "/battlelog"

response = requests.get(BASE_URL+PLAYERS+t,headers={'Authorization' : 'Bearer {}'.format(LAPTOP_KEY)})
c = response.status_code
print(response)
if c == 200:
    # 200 Indicates a Valid response
    response = response.json()
    print(response['name'])
    print(response['currentFavouriteCard']['iconUrls']['medium'])
elif c == 401:
    print("API Key is not Authorized")
elif c == 404:
    if response.reason == 'Not Found':
        print("The tag you attempted to lookup does not exist!")
    else:
        print(response.reason)
        print("Tried to request something that does not exist")


def commands_response():
    embd = discord.Embed(title="ClashAPI Commands",
                         description="Welcome to the Clash Royale section of my bot!\n*This is in the very early stages of development*\nCommands:\n$clash `")
    return embd

