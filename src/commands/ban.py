import discord
from discord import app_commands
from discord.ext import commands


class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a member")
    @app_commands.describe(
        member="Member to ban",
        days="Days of message to delete",
        reason="Reason of ban",
    )
    @app_commands.checks.bot_has_permissions(ban_members=True)
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        days: app_commands.Range[int, 0, None],
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
            await interaction.followup.send(
                "You can't ban yourself silly.", ephemeral=True
            )
            return

        if member.id == self.bot.user.id:
            await interaction.followup.send("You can't ban me silly.", ephemeral=True)
            return

        await member.ban(reason=reason, delete_message_days=days)
        await interaction.followup.send(
            f"{member.mention} has been banned. Reason: {reason}"
        )

    @app_commands.command(name="unban", description="Unban a member with ID")
    @app_commands.describe(user_id="User ID to unban")
    @app_commands.checks.bot_has_permissions(ban_members=True)
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(
        self,
        interaction: discord.Interaction,
        user_id: discord.User,
    ):
        await interaction.response.defer(ephemeral=True)

        if not interaction.guild:
            await interaction.followup.send("You can only run this within a guild")
            return

        try:
            user = await self.bot.fetch_user(user_id)
            await interaction.guild.unban(user)
            await interaction.followup.send(f"{user.mention} has been unbanned.")
        except discord.NotFound:
            await interaction.followup.send(
                "User not found or not banned.", ephemeral=True
            )


async def setup(bot):
    await bot.add_cog(BanCog(bot))
