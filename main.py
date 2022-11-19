import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
from gtts import gTTS
import random
import datetime
import string
import asyncio
import json
import requests
import urllib
import os


class SELFBOT():
    __version__ = 1


with open("cong.json") as f:
    j = json.load(f)
    token = j["token"]
    password = j["password"]
    prefix = j["prefix"]
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command("help")

@client.event
async def on_ready():
    print(Fore.GREEN + f"""
{Fore.GREEN}\n\nLogged In As This Random: {Fore.RED}[{Fore.BLUE}{client.user.name}#{client.user.discriminator}{Fore.RED}]"""
          )

@client.command()
async def game(ctx):
    await ctx.message.delete()
    await client.change_presence(
    	activity=discord.Activity(type=discord.ActivityType.playing, name='Смерть - предел мечтаний'))

@client.command()
async def stream(ctx):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Streaming(name='Смерть - предел мечтаний', url="https://twitch.tv/404"))

@client.command()
async def listen(ctx):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listen, name='Смерть - предел мечтаний'))


@client.command()
async def watch(ctx):
    await ctx.message.delete()
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watch, name='Смерть - предел мечтаний'))



@client.command()
async def clear(ctx):
    await ctx.message.delete()
    await client.change_presence(status=discord.Status.dnd)

client.run(token, bot=False)
