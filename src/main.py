import discord
import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


async def load_cogs():
    if not os.path.exists('src'):
        raise FileNotFoundError(
            'Source directory does not exist, make sure to run this outside src.')

    for folder in ["commands", "events"]:
        for filename in os.listdir(f"src/{folder}"):
            if filename.endswith(".py") and not filename.startswith("_"):
                await bot.load_extension(f"{folder}.{filename[:-3]}")

async def main():
    if not token:
        raise ValueError("empty token provided.")

    await load_cogs()
    await bot.start(token)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('⛔ Shutting down')
        exit(0)
    except Exception as exc:
        raise Exception(exc)
