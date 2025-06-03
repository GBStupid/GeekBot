import discord
from discord import app_commands
from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a member")
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = "No reason provided",
        dry_run: bool = False,
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

        embed = discord.Embed(
            title="you have been banned",
            description=f"reason: {reason}",
            color=discord.Color.red(),
        )

        embed.set_footer(text=f"from: {interaction.guild.name}")

        try:
            await member.send(embed=embed)
        except discord.Forbidden:
            pass  # can't dm them

        try:
            if not dry_run:
                await member.ban(reason=reason)
            await interaction.followup.send(
                f"{member.mention} has been banned. Reason: {reason}"
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "I don't have permission to ban this user.", ephemeral=True
            )

    @app_commands.command(name="unban", description="Unban a member with ID")
    async def unban(
        self,
        interaction: discord.Interaction,
        user_id: discord.User,
        dry_run: bool = False,
    ):
        await interaction.response.defer(ephemeral=True)

        if not interaction.guild:
            await interaction.followup.send("You can only run this within a guild")
            return

        try:
            user = await self.bot.fetch_user(user_id)
            if not dry_run:
                await interaction.guild.unban(user)
            await interaction.followup.send(f"{user.mention} has been unbanned.")
        except discord.NotFound:
            await interaction.followup.send(
                "User not found or not banned.", ephemeral=True
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "I don't have permission to unban this user.", ephemeral=True
            )


async def setup(bot):
    await bot.add_cog(BanCog(bot))
