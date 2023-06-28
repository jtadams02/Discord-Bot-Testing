# No Idea How This Will Work
import requests

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkN2Y2ZDFlLWVjNjktNGJkOS1iNjQ3LTFhM2U2OTFhZGI2OCIsImlhdCI6MTY4NzkwOTkzMSwic3ViIjoiZGV2ZWxvcGVyLzlkYjBiY2Q3LTU4MjAtNmRlMS1iOGNlLTQ1OWM4NDEwNGMxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNC4xNC4yNDcuMTczIl0sInR5cGUiOiJjbGllbnQifV19.3_NJmRz_o6AuhWJErW8ASjw0ARSQugzjZAwby8Sy0iZoEPkCxnIiJMePg0BuRuPAPE5NF60vt83jgduqeL89NA"

# Lets Test it out

BASE_URL = "https://api.clashroyale.com/v1/"

PLAYERS = "playes/%23"

t = '8VGUUC0J'

rsponse = requests.get(BASE_URL+PLAYERS+t,headers={'Authorization' : 'Bearer {}'.format(API_KEY)})

print(rsponse)
