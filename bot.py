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

'''
br = Broswer()
url = "https://smite.guru"
br.open(url)
'''

@bot.event
async def on_ready():
    '''
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    '''

    guild = discord.utils.get(bot.guilds, name=GUILD)
     
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    # Need privileged intent to see guild members

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome new Mongaloid, {member.name}.'
    )


'''
@bot.command
async def on_message(message):
    if message.author == client.user:
        return
'''

@bot.command(name='gay', help='Use this command to find the gayest member of the server')
async def gay(ctx):
    #locations = ["Phoenix", 'Tustin', 'Winslow', 'Tuscon', 'Mesa', 'Jungle', 'Duo Lane', 'Coral Highlands', 'Astera', 'The \"park\"', 'Spectating']
    #response = "Christopher's current location: "
    mongs = ["gAyMC", "yourNEMisjeff", "The Carry", "XJewlanque", "Raisin Branz"]
    response = random.choice(mongs)
    response = response + " is currently the most gayest"
    await ctx.channel.send(response)
    
    #level = random.randint(1, 999999)
    #await ctx.channel.send(f"Jake's simp level: {level}")


@bot.command(name='weak', help='Finds elemental weaknesses of the given monster. Make sure to capitalize and spell correctly.')
async def weak(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')

    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    
    for result in results_all:
        if 'Weakest to' in result.text:
            await ctx.channel.send(result.text)


@bot.command(name='weak_detailed', help='Lists elemental weaknesses')
async def weak_detailed(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    results_all = soup.find_all('table', class_ = 'wikitable')
    
    for result in results_all:
        if ('Element Weakness Damage Data' in result.text):
            tr_list = result.find_all('tr')
            table = result
            break
    
    tr_list.pop(0)
    tr_list.pop(0)

    elements = {0 : "Fire", 1 : "Water", 2 : "Thunder", 3 : "Ice", 4 : "Dragon"}

    for tr in tr_list:
        td_list = tr.find_all('td')
        await ctx.channel.send(td_list[0].text)
        td_list.pop(0)
        i=0
        output = ''
        for td in td_list:
            output = output + elements[i] + ': ' + td.text
            i = i+1
        await ctx.channel.send(output)

    
bot.run(TOKEN)
