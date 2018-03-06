import discord
import json

with open("client_data.json", "r") as f:
    clientdata = json.load(f)

myself = discord.Client()

@myself.event
async def on_message(message):
    print(message.content, message.channel)