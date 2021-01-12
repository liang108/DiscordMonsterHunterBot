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
    greetings = ('Howdy there, Pard! Ready to eat, err, I mean hunt some monsters?', 'Yo Pard! Just letting ya know, if your Palico acts up again it might be my next lunch...',
                 'Salutations Pard! The Field Team Leader says I\'m weird for liking monster foods, I just think it\'s funny how he\'s never successfully hunted a monster',
                 'How you doin\' Pard! Do you think I put on weight recently?...',
                 'Hey Pard! Ever think about how the Serious Handler is incredibly inferior to me in both weight and intellect?')
    await channel.send(random.choice(greetings))

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
    await channel.send('I\'m feelin\' hungry, gotta go eat! Later, Pard!')

@bot.command(name='weak', help='Finds elemental weaknesses of the given monster.')
async def weak(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    phrases = ('Mmm, ' + monster + '!\n', 'Oh, ' + monster + '? I love the taste of ' + monster + '!\n', 'Ooh, Pard, bring me back some ' + monster + '!\n'
               'I\'ve always wanted to try ' + monster + ' stew!\n', monster + ' - its tail is so tasty! Break it for me please.\n',
               monster + '... \*drools\*\n', 'I can\'t wait to taste some ' + monster + '... B)\n')
    found = False
    await ctx.channel.send(random.choice(phrases))
    for result in results_all:
        if 'Weakest to' in result.text:
            found = True
            await ctx.channel.send(result.text)
            break
    if found == False:
        await ctx.channel.send('Sorry, Pard, I couldn\'t find that monster! Make sure to replace spaces with \"_\" and capitalize!')

    
@bot.command(name='type', help='Get the given monster\'s elements.')
async def type(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    phrases = ('Mmm, ' + monster + '!\n', 'Oh, ' + monster + '? I love the taste of ' + monster + '!\n', 'Ooh, Pard, bring me back some ' + monster + '!\n',
               'I\'ve always wanted to try '  + monster + ' stew!\n', monster + ' - its tail is so tasty! Break it for me please.\n',
               monster + '... \*drools\*\n', 'I can\'t wait to taste some ' + monster + '... B)\n')    
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    found = False
    await ctx.channel.send(random.choice(phrases))
    for result in results_all:
        if 'Elements' in result.text:
            found = True
            await ctx.channel.send(result.text)
            break
    if found == False:
        await ctx.channel.send('Sorry, Pard, I couldn\'t find that monster! Make sure to replace spaces with \"_\" and capitalize!')

    
@bot.command(name='ailments', help='Find which ailments the given monster can apply')
async def ailments(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    phrases = ('Mmm, ' + monster + '!\n', 'Oh, ' + monster + '? I love the taste of ' + monster + '!', 'Ooh, Pard, bring me back some ' + monster + '!\n',
               'I\'ve always wanted to try '  + monster + ' stew!\n', monster + ' - its tail is so tasty! Break it for me please.\n',
               monster + '... \*drools\*\n', 'I can\'t wait to taste some ' + monster + '... B)\n')
    found = False
    await ctx.channel.send(random.choice(phrases))
    for result in results_all:
        if 'Ailments' in result.text:
            found = True
            await ctx.channel.send(result.text)
            break
    if found == False:
        await ctx.channel.send('Sorry, Pard, I couldn\'t find that monster! Make sure to replace spaces with \"_\" and capitalize!')


@bot.command(name='all', help='Get a monster\'s weaknesses, elements, and ailments')
async def all(ctx, monster):
    url = 'https://monsterhunter.fandom.com/wiki/' + monster
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results_all = soup.find_all(class_ = 'pi-item pi-data pi-item-spacing pi-border-color')
    phrases = ('Mmm, ' + monster + '!\n', 'Oh, ' + monster + '? I love the taste of ' + monster + '!\n', 'Ooh, Pard, bring me back some ' + monster + '!\n', 'I\'ve always wanted to try '  + monster + ' stew!\n',
               monster + ' - its tail is so tasty! Break it for me please.\n', monster + '... \*drools\*\n', 'I can\'t wait to taste some ' + monster + '... B)\n')
    found_count = 0
    for result in results_all:
        if 'Weakest to' in result.text:
            await ctx.channel.send(result.text)
            found_count = found_count + 1
            next
        if 'Elements' in result.text:
            await ctx.channel.send(random.choice(phrases))
            await ctx.channel.send(result.text)
            found_count = found_count + 1
            next
        if 'Ailments' in result.text:
            await ctx.channel.send(result.text)
            found_count = found_count + 1
            next

    if found_count != 3:
        await ctx.channel.send('Sorry, Pard! Couldn\'t find all the info on that monster.')
  
bot.run(TOKEN)
