import discord
from discord import app_commands
from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick a member from the server")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("you can't kick yourself.", ephemeral=True)
            return

        if member == self.bot.user:
            await interaction.response.send_message("you can't kick me.", ephemeral=True)
            return

        # create the embed for the dm
        reason_text = reason if reason else "unknown"
        embed = discord.Embed(
            title="you have been kicked",
            description=f"reason: {reason_text}",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"from: {interaction.guild.name}")

        try:
            await member.send(embed=embed)
        except discord.Forbidden:
            pass  # can't dm the user, just ignore

        try:
            await member.kick(reason=reason_text)
            await interaction.response.send_message(f"{member.mention} has been kicked. reason: {reason_text}")
        except discord.Forbidden:
            await interaction.response.send_message("i don't have permission to kick this user.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(KickCog(bot))
