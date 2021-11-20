# encoding: utf-8
__author__ = "Rayyan S."
__copyright__ = "Copyright 2021, Rayyan S."
__version__ = "1.0"
__email__ = "rayyanhps@gmail.com"
__status__ = "Production"

import os
import sys, traceback

from dotenv import load_dotenv

import discord
from discord.ext import commands, tasks
from discord.utils import find
from discord_components import DiscordComponents, Button

import asyncio
import asyncpg

def get_prefix(bot, message):
    prefixes = ['-', '.']
    if not message.guild:
        return '!'
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)

initial_extensions = [
                    'cogs.Characters',
                    'cogs.Campaigns',
                    'cogs.Post',
                    'cogs.Roll',
                    'cogs.CommandErrorHandler',
                    'cogs.Timezone']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

def load_env():
    dotenv_path = os.path.join('env', '.env')
    load_dotenv(dotenv_path)
    token = os.getenv("DISCORD_TOKEN")
    return token

@bot.event
async def on_ready():
    await asyncio.sleep(0.1)
    DiscordComponents(bot)
    print("""\
                          _                  _   _              
 __      ____ ___   _____| | ___ _ __   __ _| |_| |__  \    /\  
 \ \ /\ / / _` \ \ / / _ \ |/ _ \ '_ \ / _` | __| '_ \  )  ( ') 
  \ V  V / (_| |\ V /  __/ |  __/ | | | (_| | |_| | | |(  /  )  
   \_/\_/ \__,_| \_/ \___|_|\___|_| |_|\__, |\__|_| |_| \(__)|  
                                       |___/  v.1.0 discord.py         
+ v.1.0 - created base folder structure
"ASCII Art is not out of practice." - Benjamin Button
""")

def run_bot():
    try:
        bot.run(load_env())
    except KeyboardInterrupt:
        bot.logout()

loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())