import discord
from discord import app_commands
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="❓ bot commands",
            description="here are the available slash commands:",
            color=discord.Color.yellow(),
        )
        embed.add_field(name="/ping", value="shows bot latency", inline=False)
        embed.add_field(name="/serverstats", value="shows server stats", inline=False)
        embed.add_field(name="/help", value="shows this help message", inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(HelpCog(bot))
