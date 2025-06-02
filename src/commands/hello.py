import discord
from discord import app_commands

async def setup(bot):
    @app_commands.command(name="helloworld", description="hello world")
    async def helloworld(interaction: discord.Interaction):
        await interaction.response.send_message("hello world")

    bot.tree.add_command(helloworld)

