# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import spoonacular as sp
import time

load_dotenv()

TOKEN = os.getenv('TOKEN')
SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')
spoon = sp.API(SPOONACULAR_API_KEY)

ready_members = {}
show_edits = os.getenv('SHOW_EDITS', True)
show_deletes = os.getenv('SHOW_DELETES', True)

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
                ready_members[member.name + '#' + member.discriminator] = False
    
    print(f'Guild Members: {ready_members}')
    print(f'Show edits: {show_edits}\nShow deletes: {show_deletes}')


@bot.command()
async def ready(ctx):
    author = str(ctx.author)
    print(f'Readied Up: {ready_members}')
    print(f'Author: {author}')

    ready_members[author] = not ready_members[author]
    if ready_members[author]:
        await ctx.send(f'{author} readied up.')
    else:
        await ctx.send(f'{author} is no longer ready.')

    if all(value == True for value in ready_members.values()):
        await ctx.send('All members ready\nThe pact may proceed.')


@bot.command()
async def recipe(ctx, *args):
    user_arguments = ', '.join(args)

    if len(user_arguments) < 1:
        user_arguments = None
    
    print(f'Getting random recipe with user tags: {user_arguments}')

    try:
        response = spoon.get_random_recipes(tags=user_arguments, number=1)
        data = response.json()
        recipe = data['recipes'][0]
        
        embed = discord.Embed(title=recipe['title'], url=recipe['sourceUrl'])
        embed.set_thumbnail(url=recipe['image'])
        await ctx.send(embed=embed)
    except:
        await ctx.send('Failed to get recipe, try using a different keyword, or try again later')

@bot.command()
async def edit(ctx):
    global show_edits
    show_edits = not show_edits
    if show_edits:
        await ctx.send('I am currently displaying edits')
    else:
        await ctx.send('I am no longer displaying edits')


@bot.command()
async def delete(ctx):
    global show_deletes
    show_deletes = not show_deletes
    if show_deletes:
        await ctx.send('I am currently displaying deleted messages')
    else:
        await ctx.send('I am no longer displaying deleted messages')


@bot.event
async def on_message_delete(message):
    global show_deletes
    if show_deletes:
        t = time.localtime()
        current_time = current_time = time.strftime("%H:%M:%S", t)
        embed = discord.Embed()
        embed.add_field(name=f'{message.author} deleted the following message at {current_time}:', value=message.content)
        await message.channel.send(embed=embed)


@bot.event
async def on_message_edit(message_before, message_after):
    global show_edits
    if show_edits:         
        embed = discord.Embed(title=f'{message_before.author} made an edit!')
        embed.add_field(name=f'Before:', value=message_before.content, inline=False)
        embed.add_field(name=f'Edited:', value=message_after.content, inline=False)
        await message_before.channel.send(embed=embed)


@bot.command()
async def bot_help(ctx):
    embed = discord.Embed(title='Available Commands', color=discord.Color.blue())
    embed.add_field(
        name='!ready', value='Use the !ready to command to ready up, or to un ready. When all members are ready, I will notify the channel.', inline=False)
    embed.add_field(
        name='!recipe', value='Use the reciepe to generate a random recipe. Add tage separated by spaces if you wish to refine the search like so: `!recipe vegatarian desert`', inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)