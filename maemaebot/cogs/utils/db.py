import asyncio
import asyncpg
from dotenv import load_dotenv
import os
import sys, traceback

def load_config():
        dotenv_path = os.path.join('env', '.env')
        load_dotenv(dotenv_path)
        config = {
            "user": os.getenv("DBUSER"), 
            "password": os.getenv("DBPW"), 
            "database": os.getenv("DB"), 
            "host": os.getenv("HOST")
        }
        return config

async def fetch_value(query, *args):
    config = load_config()
    con = await asyncpg.connect(**config)
    value = await con.fetchval(query, *args)
    await con.close()
    return value

async def fetch_row(query, *args):
    config = load_config()
    con = await asyncpg.connect(**config)
    value = await con.fetchrow(query, *args)
    await con.close()
    return value

async def fetch(query, *args):
    config = load_config()
    con = await asyncpg.connect(**config)
    value = await con.fetch(query, *args)
    await con.close()
    return value

async def execute(query, *args):
    config = load_config()
    con = await asyncpg.connect(**config)
    value = await con.execute(query, *args)
    await con.close()
    return value