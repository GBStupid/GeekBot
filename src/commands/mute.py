from datetime import timedelta

import discord
from discord import app_commands

MAX_TIMEOUT_MINUTES = 40320  # 28 days
TIME_UNITS = {
    "seconds": "seconds",
    "minutes": "minutes",
    "hours": "hours",
    "days": "days",
}
UNIT_TO_KWARG = {
    "seconds": "seconds",
    "minutes": "minutes",
    "hours": "hours",
    "days": "days",
}
UNIT_LIMITS = {
    "seconds": MAX_TIMEOUT_MINUTES * 60,
    "minutes": MAX_TIMEOUT_MINUTES,
    "hours": MAX_TIMEOUT_MINUTES // 60,
    "days": MAX_TIMEOUT_MINUTES // (60 * 24),
}


async def setup(bot):
    @app_commands.command(
        name="mute",
        description="Timeout a user",
    )
    @app_commands.describe(
        user="The user to mute",
        duration="Duration (see unit)",
        unit="Unit of time (seconds, minutes, hours, days)",
    )
    @app_commands.choices(
        unit=[
            app_commands.Choice(name="seconds", value="seconds"),
            app_commands.Choice(name="minutes", value="minutes"),
            app_commands.Choice(name="hours", value="hours"),
            app_commands.Choice(name="days", value="days"),
        ]
    )
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(
        interaction: discord.Interaction,
        user: discord.Member,
        duration: int,
        unit: app_commands.Choice[str],
    ):
        await interaction.response.defer(ephemeral=True)

        if not interaction.guild:
            await interaction.followup.send("You can only run this within a guild")
            return

        unit_value = unit.value
        max_value = UNIT_LIMITS[unit_value]
        if not (0 < duration <= max_value):
            if duration <= 0:
                error_message = "duration must be greater than 0."
            else:
                error_message = (
                    f"duration can't exceed {max_value} {unit_value} (28 days max)."
                )
            await interaction.followup.send(error_message, ephemeral=True)
            return

        try:
            td_kwargs = {UNIT_TO_KWARG[unit_value]: duration}
            await user.timeout(timedelta(**td_kwargs))
            await interaction.followup.send(
                f"🔇 muted {user.mention} for `{duration}` {unit_value}."
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "I don't have permission to mute that user.", ephemeral=True
            )

    bot.tree.add_command(mute)
