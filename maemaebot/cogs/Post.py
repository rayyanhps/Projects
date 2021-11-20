import requests

import os
import sys, traceback

import random as rand
import asyncio
import asyncpg

import discord
from discord.ext import commands

from dotenv import load_dotenv

dotenv_path = os.path.join('env', '.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv("DISCORD_TOKEN")
DBUSER = os.getenv("DBUSER")
DBPW = os.getenv("DBPW")
DB = os.getenv("DB")
HOST = os.getenv("HOST")
config = {"user": DBUSER, "password": DBPW, "database": DB, "host": HOST}

class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        keyword_list_1 = ['MAE', 'MAMAS', 'KITTEN', 'BABYGIRL']
        if any([keyword in message.content.upper() for keyword in keyword_list_1]) and message.author != self.bot:
            await message.channel.send("ᵐᵉᵒʷ")


    @commands.command(name='post', aliases=['rp'], pass_context=False)
    @commands.guild_only()
    async def post(self, ctx, *args):
        #immediately deletes message on post
        await ctx.message.delete()
        db = await asyncpg.connect(**config)
        query = "SELECT * FROM dwh_master.user_characters WHERE user_id = $1 and active;"
        row = await db.fetchrow(query, ctx.author.id)
        #get the webhook 
        await ctx.channel.create_webhook(name = 'poster')
        hook = discord.utils.get(await ctx.channel.webhooks(), name = 'poster')
        text = ' '.join(args)
        await hook.send(content=text, username=row['character_username'], avatar_url=row['avatar'], tts=False, file=None, files=None, embed=None, allowed_mentions=None)
        await hook.delete()
        

def setup(bot):
    bot.add_cog(Post(bot))