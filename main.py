# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

readyMembers = {}

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    for guild in bot.guilds:
        for member in guild.members:
            if not member.name == 'playground-bot':
                readyMembers[member.name + '#' + member.discriminator] = False
    print(f'Guild Members: {readyMembers}')



@bot.command()
async def copycat(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def ready(ctx):
    author = str(ctx.author)
    print(f'Readied Up: {readyMembers}')
    print(f'Author: {author}')


    readyMembers[author] = not readyMembers[author]
    if readyMembers[author]:    
        await ctx.send(f'{author} readied up.')
    else:
        await ctx.send(f'{author} is no longer ready.')

    if all(value == True for value in readyMembers.values()):
        await ctx.send('All members ready\nThe pact may proceed.')
    print(readyMembers)


bot.run(TOKEN)
