import discord
from discord import app_commands


@app_commands.command(
    name="unmute",
    description="Remove a timeout from a user",
)
@app_commands.describe(
    user="The user to unmute"
)
@app_commands.checks.has_permissions(moderate_members=True)
async def unmute(
    interaction: discord.Interaction,
    user: discord.Member,
):
    await interaction.response.defer(ephemeral=True)

    if not interaction.guild:
        await interaction.followup.send("You can only run this within a server.")
        return

    try:
        await user.timeout(None)
        await interaction.followup.send(f"✅ {user.mention} has been unmuted.")
    except discord.Forbidden:
        await interaction.followup.send(
            "I do not have permission to unmute this user.", ephemeral=True
        )
    except discord.HTTPException:
        await interaction.followup.send(
            "Failed to unmute the user. Try again later.", ephemeral=True
        )


async def setup(bot: discord.Client):
    bot.tree.add_command(unmute)

