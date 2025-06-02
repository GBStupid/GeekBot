import discord
from discord import app_commands
from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick a member from the server")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        if member == interaction.user:
            await interaction.response.send_message("You can't kick yourself.", ephemeral=True)
            return

        if member == self.bot.user:
            await interaction.response.send_message("You can't kick me.", ephemeral=True)
            return

        try:
            await member.kick(reason=reason)
            await interaction.response.send_message(f"{member.mention} has been kicked. Reason: {reason}")
        except discord.Forbidden:
            await interaction.response.send_message("I don't have permission to kick this user.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(KickCog(bot))

