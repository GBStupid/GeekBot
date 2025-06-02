import discord
from discord import app_commands
from discord.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Displays bot's latency")
    async def ping(self, interaction: discord.Interaction):
        l_ms = round(self.bot.latency * 1000)
        embed = discord.Embed(
                title="🏓 pong!",
                description=f"Latency: **{l_ms}ms**",
                color=discord.Color.green()
                )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(PingCog(bot))
