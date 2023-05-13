import discord
import asyncio


# Get the bot token
TOKEN = "MTEwNjA0NTE4NDE2NjM1MDk1OA.GvyVxV.uAqSPiwHtyA_PBTHRmNCKZEzfLQRJw5UjYmNEA"

# Create a Discord client

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.members = True

# Define a function to kick the user
def kick_user(user_id):
    # Get the user
    user = client.get_user(user_id)

    # Get the user's voice channel
    voice_channel = user.voice_channel

    # If the user is in a voice channel, kick them
    if voice_channel:
        voice_channel.kick(user)

# Define a function to send a message to the channel
async def send_message(channel, message):
    # Send the message to the channel
    await channel.send(message)

# When the bot is ready, send a message to the channel
@client.event
async def on_ready():
    # Send a message to the channel
    await send_message(client.get_channel(589144738637021205), "Я здесь чтобы кикать баса!")

# When the command /kicker is used, kick the user
@client.event
async def on_message(message):
    # If the command is /kicker
    if message.content == "/kicker":
        # Kick the user
        kick_user(message.author.id)
        # Send a message to the channel
        await send_message(message.channel, "Бас был кикнут!")

# Run the bot
client.run(TOKEN)
