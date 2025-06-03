from datetime import timedelta

import discord
from discord import app_commands

MAX_TIMEOUT_MINUTES = 40320  # 28 days


async def setup(bot):

    @app_commands.command(name="mute", description="Timeout a user")
    @app_commands.describe(
        user="The user to mute", duration="Duration in minutes (max: 40320)"
    )
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(
        interaction: discord.Interaction, user: discord.Member, duration: int
    ):
        await interaction.response.defer(ephemeral=True)

        if not interaction.guild:
            await interaction.followup.send("You can only run this within a guild")
            return

        if not (0 < duration <= MAX_TIMEOUT_MINUTES):
            error_message = (
                "duration must be greater than 0."
                if duration <= 0
                else "duration can't exceed 40320 minutes (28 days)."
            )
            await interaction.followup.send(error_message, ephemeral=True)
            return

        try:
            await user.timeout(timedelta(minutes=duration))
            await interaction.followup.send(
                f"🔇 muted {user.mention} for `{duration}` minutes."
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "I don't have permission to mute that user.", ephemeral=True
            )

    bot.tree.add_command(mute)
