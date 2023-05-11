import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def kicker(ctx):
    member = discord.utils.get(ctx.guild.members, name='Beanskers#5403')
    if member is not None:
        await member.edit(voice_channel=None)
        await ctx.send(f"{member.mention} был заблокирован в голосовых каналах на 5 минут.")
        await asyncio.sleep(300) # 300 секунд = 5 минут
        await ctx.send(f"{member.mention} может снова использовать голосовые каналы.")
    else:
        await ctx.send("Пользователь не найден.")
#вот это менять если ты у себя разворачивать бота хочешь
bot.run('')
