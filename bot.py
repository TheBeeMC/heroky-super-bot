import discord  # sniper.py
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging
command_prefix = '+'
bot = commands.Bot(command_prefix)
description = 'Sniper made by Lizard'

@bot.event
async def on_message(message):
    if message.content.startswith('+queue'):
        embed = discord.Embed(title="SERVICE STATUS", description="", colour=1742064)
        embed.set_author(name='Authentication service is currently being fixed', icon_url='')
        embed.add_field(name='We will be back soon!', value='Sniper session service is not healthy and will be fix asap!')
        embed.set_footer(text='Sniper made by Lizard')
        await message.channel.send(embed=embed)
    if message.content.startswith('+checktokens'):
        embed = discord.Embed(title='you have have 0 tokens', description='If you want more pm lizard', color=1742064)
        embed.set_author(name='Service is currently down and will be back as soon as possible', icon_url='')
        embed.add_field(name='Tokens can beat other queued snipes', value='the % chance is 0 of sniping a name', inline=True)
        embed.set_footer(text='sniper coded by Lizard')
        await message.channel.send(embed=embed)
    if message.content.startswith('+snipecheck'):
        await message.channel.send("The names that are taken are")
        await message.channel.send("Heaven")
        await message.channel.send("Shower")
        await message.channel.send("Bone")
        await message.channel.send("Spifey")
        await message.channel.send("Thot")
        await message.channel.send("Snore: From Nate")
        await message.channel.send("Coyote")
        await message.channel.send("Spop: From CHRIS")
        await message.channel.send("Warning")
        await message.channel.send("Base")
        await message.channel.send("IGN")
        await message.channel.send("Smoothed")
        await message.channel.send("All these names are taken and cannot be taken by Tokens")
        print('Discord bot made by lizard')
    if message.content.startswith('check'):
        await message.channel.send('Setting name AdolfFuhrer has been sniped')

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name='with og names'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name='+help | coded by lizard'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name='with my sniper'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name='with a fidget spinner'))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('NDc3NDM3ODAyNTE5MzMwODE2.Dk8LNQ.jLHAALrH8H-OUFHlGrVYsL59lBc')
