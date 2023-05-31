import discord

import json
from datetime import timedelta



###### JSON ###########
# Load the token from the .json file into a Python variable

with open("data.json", "r") as f:
    data = json.load(f)
    token = data["token"]
    Roles = data["roles"]


######## DISCORD BOT ##############
# Idk what this does, but it only worked when I copy pasted it
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}#{client.user.discriminator}')

# Invite check
@client.event
async def on_invite_create(invite):
    global Roles
    if invite.max_age == 0:
        # Check if user is mod
        member = invite.guild.get_member(invite.inviter.id)
        for role in member.roles:
            if role.id in Roles:
               #print("Member is mod\n")
                return # Return if member is mod/admin/etc

        # Deletes invite
        await invite.delete()
        print(f"Deleted permanent invite: {invite.code}")

        # DM user
        new_invite = await invite.channel.create_invite(max_age=7*24*60*60) # Create 7 day invite
        new_expires_at = new_invite.created_at + timedelta(seconds=invite.max_age) # Time the invite expires
        formatted_time = new_expires_at.strftime('%Y-%m-%d %H:%M:%S') # Format time
        await invite.inviter.send(f"Your invite has been deleted since we do not allow permanent invites. Instead use the following code. It expires at `{formatted_time}`.")
        await invite.inviter.send(f"<{new_invite.url}>")




client.run(token)