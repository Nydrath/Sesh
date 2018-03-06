import discord
import json

SESHLOG_CHANNEL_ID = "420378939391868938"
MODERATOR_ROLE_ID = "270985489761304577"

with open("client_data.json", "r") as f:
    clientdata = json.load(f)

myself = discord.Client()

@myself.event
async def on_message(message):
    if myself.user in message.mentions:
        if MODERATOR_ROLE_ID in [role.id for role in message.author.roles]:
            if "list" in message.content and len(message.role_mentions) > 0:
                for role in message.role_mentions:
                    await myself.send_message(message.channel, role.mention+":")
                    for member in message.server.members:
                        if role in member.roles:
                            nickname = ""
                            if member.nick != None:
                                nickname = " [{0}]".format(member.nick)
                            await myself.send_message(message.channel, member.mention+nickname)
                    await myself.send_message(message.channel, "Done.")


@myself.event
async def on_member_join(member):
    channels = member.server.channels
    botlog = [channel for channel in channels if channel.id == SESHLOG_CHANNEL_ID][0]
    await myself.send_message(botlog, member.mention+" has joined the server.")

@myself.event
async def on_member_remove(member):
    channels = member.server.channels
    botlog = [channel for channel in channels if channel.id == SESHLOG_CHANNEL_ID][0]
    await myself.send_message(botlog, member.mention + " has left the server.")

myself.run(clientdata["token"])