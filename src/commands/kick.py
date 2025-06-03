import discord
from discord import app_commands
from discord.ext import commands


class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick a member from the server")
    @app_commands.describe(member="Member to kick", reason="Reason for kick")
    @app_commands.checks.bot_has_permissions(kick_members=True)
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided",
    ):
        await interaction.response.defer(ephemeral=True)

        if not interaction.guild:
            await interaction.followup.send("You can only run this within a guild")
            return

        if not member:
            await interaction.followup.send("Member not provided")
            return

        if member.id == interaction.user.id:
            await interaction.followup.send("You can't kick yourself.", ephemeral=True)
            return

        if member.id == self.bot.user.id:
            await interaction.followup.send("You can't kick me.", ephemeral=True)
            return

        await member.kick(reason=reason)
        await interaction.followup.send(
            f"{member.mention} has been kicked. Reason: {reason}"
        )


async def setup(bot):
    await bot.add_cog(KickCog(bot))
