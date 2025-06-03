import discord
from discord import app_commands
from discord.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Displays bot's latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = discord.Embed(
            title="🏓 pong!",
            description=f"Latency: **{round(self.bot.latency * 1000)}ms**",
            color=discord.Color.green(),
        )
        await interaction.followup.send(embed=embed)


async def setup(bot):
    await bot.add_cog(PingCog(bot))
