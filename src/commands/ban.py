import discord
from discord import app_commands
from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a member from the server")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await interaction.response.defer(ephemeral=True)  # tells discord you're working

        if member == interaction.user:
            await interaction.followup.send("You can't ban yourself silly.", ephemeral=True)
            return

        if member == self.bot.user:
            await interaction.followup.send("You can't ban me silly.", ephemeral=True)
            return

        reason_text = reason if reason else "unknown"
        embed = discord.Embed(
            title="you have been banned",
            description=f"reason: {reason_text}",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"from: {interaction.guild.name}")

        try:
            await member.send(embed=embed)
        except discord.Forbidden:
            pass  # can't dm them

        try:
            await member.ban(reason=reason_text)
            await interaction.followup.send(f"{member.mention} has been banned. Reason: {reason_text}")
        except discord.Forbidden:
            await interaction.followup.send("I don't have permission to ban this user.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(BanCog(bot))
