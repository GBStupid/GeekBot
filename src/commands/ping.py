import discord
from discord import app_commands

async def setup(bot):
    @app_commands.command(name="ping", description="Displays bot's latency")
    async def ping(interaction: discord.Interaction):
        l_ms = round(bot.latency * 1000)
        embed = discord.Embed(
                title="🏓 pong!",
                description=f"Latency: **{l_ms}ms**",
                color=discord.Color.green()
                )
        await interaction.response.send_message(embed=embed)

    bot.tree.add_command(ping)
