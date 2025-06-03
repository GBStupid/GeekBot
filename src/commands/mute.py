import discord
from discord import app_commands
from datetime import timedelta

MAX_TIMEOUT_MINUTES = 40320  # 28 days

async def setup(bot):
    @app_commands.command(name="mute", description="timeout (mute) a user for a duration in minutes")
    @app_commands.describe(user="the user to mute", duration="duration in minutes (max: 40320)")
    async def mute(interaction: discord.Interaction, user: discord.Member, duration: int):
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("you don’t have permission to mute users.", ephemeral=True)
            return

        if duration <= 0:
            await interaction.response.send_message("duration must be greater than 0.", ephemeral=True)
            return

        if duration > MAX_TIMEOUT_MINUTES:
            await interaction.response.send_message("duration can't exceed 40320 minutes (28 days).", ephemeral=True)
            return

        try:
            await user.timeout(timedelta(minutes=duration))
            await interaction.response.send_message(f"🔇 muted {user.mention} for `{duration}` minutes.")
        except discord.Forbidden:
            await interaction.response.send_message("i don’t have permission to mute that user.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"something went wrong: `{e}`", ephemeral=True)

    bot.tree.add_command(mute)
