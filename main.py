import discord
import json


###### JSON ###########
# Load the token from the .json file into a Python variable

with open("data.json", "r") as f:
    data = json.load(f)
    token = data["token"]



######## DISCORD BOT ##############
# Idk what this does, but it only worked when I copy pasted it
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



client.run(token)