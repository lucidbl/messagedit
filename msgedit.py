import requests
import time

channel_id = input("Channel ID: ")
message_id = input("Message ID: ")
token = input("Token: ")
message1 = "volim"
message2 = "vanya"
message3 = ":hearts:"
tokenz = {"authorization":f"{token}"}

while True:
    edit = requests.patch(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers = tokenz, json={"content":f"{message1}"})
    time.sleep(1)
    edit2 = requests.patch(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers = tokenz, json={"content":f"{message2}"})
    time.sleep(1)
    edit3 = requests.patch(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers = tokenz, json={"content":f"{message3}"})
    time.sleep(1)
    
