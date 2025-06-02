import discord
import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv

from events import e_handler
from commands import c_handler

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    if not token:
        raise ValueError("empty token provided.")

    await e_handler.load_events(bot)
    await c_handler.load_commands(bot)


if __name__ == '__main__':
    asyncio.run(main())
    bot.run(token)
    
