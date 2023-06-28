# Learning how API's work!
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    print(text)

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkN2Y2ZDFlLWVjNjktNGJkOS1iNjQ3LTFhM2U2OTFhZGI2OCIsImlhdCI6MTY4NzkwOTkzMSwic3ViIjoiZGV2ZWxvcGVyLzlkYjBiY2Q3LTU4MjAtNmRlMS1iOGNlLTQ1OWM4NDEwNGMxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNC4xNC4yNDcuMTczIl0sInR5cGUiOiJjbGllbnQifV19.3_NJmRz_o6AuhWJErW8ASjw0ARSQugzjZAwby8Sy0iZoEPkCxnIiJMePg0BuRuPAPE5NF60vt83jgduqeL89NA"
LAPTOP_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJkNGRhZmQxLTVmMjYtNDc4MC1iYjU1LWM3YzEzOGEyYjcxYSIsImlhdCI6MTY4Nzk2MzAzMiwic3ViIjoiZGV2ZWxvcGVyLzlkYjBiY2Q3LTU4MjAtNmRlMS1iOGNlLTQ1OWM4NDEwNGMxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzIuNTguMTY2LjE5OCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.0UdzL4Hpofybw1o6o2aCJVFy69trrhYJFbPEYmAPHnAdYUKe09IhnRXMH64IEI67H2T4ZkXQ9DMnsqvodtmkRA"
# Lets Test it out

BASE_URL = "https://api.clashroyale.com/v1/"

PLAYERS = "players/%23"

t = '8VGUUC0J'

BATTLES = "/battlelog"

response = requests.get(BASE_URL+PLAYERS+t+BATTLES,headers={'Authorization' : 'Bearer {}'.format(LAPTOP_KEY)})
c = response.status_code

if c == 200:
    # 200 Indicates a Valid response
    response = response.json()
    print(response['name'])
elif c == 401:
    print("API Key is not Authorized")
elif c == 404:
    if response.reason == 'Not Found':
        print("The tag you attempted to lookup does not exist!")
    else:
        print(response.reason)
        print("Tried to request something that does not exist")

