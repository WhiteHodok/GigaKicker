import discord
import asyncio

bot = discord.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=[589144736229752863])  # Replace [...] with your guild id
async def iluha(ctx: discord.ApplicationContext, member: discord.Member = None):
    """Kick a user from voice chat for 5 minutes"""
    user = member or ctx.author
    if 589147800760090624 in [role.id for role in ctx.author.roles]:
        if user.voice and user.voice.channel:
            await user.move_to(None, reason="Requested by /iluha command")
            await asyncio.sleep(300)
            await ctx.respond(f"User {user.name} has been kicked from the voice channel for 5 minutes.")
        else:
            await ctx.respond(f"User {user.name} is not in a voice channel.")
    else:
        await ctx.respond("You do not have permission to use this command.")

bot.run('')


