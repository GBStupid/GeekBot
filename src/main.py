import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

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

@bot.tree.command(name="serverstats", description="shows server stats")
async def serverstats(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(
        title=f"📊 server stats for {guild.name}",
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=guild.icon.url if guild.icon else discord.Embed.Empty)
    embed.add_field(name="owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="created on", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="members", value=str(guild.member_count), inline=True)
    embed.add_field(name="boosts", value=f"level {guild.premium_tier} ({guild.premium_subscription_count} boosts)", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="help", description="shows this help message")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="❓ bot commands",
        description="here are the available slash commands:",
        color=discord.Color.yellow()
    )
    embed.add_field(name="/ping", value="shows bot latency", inline=False)
    embed.add_field(name="/helloworld", value="responds with hello world", inline=False)
    embed.add_field(name="/serverstats", value="shows server stats", inline=False)
    embed.add_field(name="/help", value="shows this help message", inline=False)
    await interaction.response.send_message(embed=embed)

if __name__ == '__main__':
    if not token:
        raise ValueError("empty token provided.")
    bot.run(token)
