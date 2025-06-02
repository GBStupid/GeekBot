import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"logged in as {bot.user}")

@bot.tree.command(name="ping", description="shows bot latency")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 pong!",
        description=f"Latency: **{latency_ms}ms**",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="helloworld", description="responds with hello world")
async def helloworld(interaction: discord.Interaction):
    await interaction.response.send_message("hello world")

bot.run(token)
