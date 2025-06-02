import discord
from discord import app_commands

async def setup(bot):
    @app_commands.command(name="help", description="shows this help message")
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

    bot.tree.add_command(help_command)

