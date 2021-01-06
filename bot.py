# bot.py
import os
import random
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    guild = discord.utils.get(bot.guilds, name=GUILD)
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send('Howdy there, Pard! Ready to eat some monsters?')
    '''
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # Need privileged intent to see guild members

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')
    '''

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome new Mongaloid, {member.name}.'
    )


@bot.event
async def on_disconnect():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send('I\'m feeling hungry, gotta go eat! Later, Pard!')


@bot.command(name='gay', help='Use this command to find the gayest member of the server')
async def gay(ctx, user):
    adjectives = ('big', 'gigantic', 'ginormous', 'huge', 'colossal', 'sizeably', 'substantially', 'comically', 'immensely', 'macroscopically', 'vastly', 'enormously', 'largely', 'cosmically', 'abysmally', 'ludicrously', 'ridiculously', 'fantastically')
    await ctx.channel.send(user + ' is ' + random.choice(adjectives) + ' gay')


@bot.command(name='weak', help='Finds elemental weaknesses of the given monster. Make sure to capitalize and spell correctly.')
async def weak(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    found = False
    for result in results_all:
        if 'Weakest to' in result.text:
            found = True
            await ctx.channel.send(result.text)
            break
    if found == False:
        await ctx.channel.send('Monster not found; make sure to replace spaces with \"_\" and capitalize')

    
@bot.command(name='type', help='Get the given monster\'s elements.')
async def type(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    found = False
    for result in results_all:
        if 'Elements' in result.text:
            found = True
            await ctx.channel.send(result.text)
            break
    if found == False:
        await ctx.channel.send('Monster not found; make sure to replace spaces with \"_\" and capitalize')

    
@bot.command(name='ailments', help='Find which ailments the given monster can apply')
async def ailments(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    found = False
    for result in results_all:
        if 'Ailments' in result.text:
            found = True
            await ctx.channel.send(result.text)
            break
    if found == False:
        await ctx.channel.send('Monster not found; make sure to replace spaces with \"_\" and capitalize')

    
bot.run(TOKEN)
