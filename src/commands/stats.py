import discord
from discord import app_commands
from discord.ext import commands


class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverstats", description="shows server stats")
    async def serverstats(self, interaction: discord.Interaction):
        await interaction.response.defer()
        if not interaction.guild:
            await interaction.followup.send("You can only run this within a guild.")
            return

        embed = discord.Embed(
            title=f"📊 server stats for {interaction.guild.name}",
            color=discord.Color.blurple(),
        )

        embed.set_thumbnail(
            url=interaction.guild.icon.url if interaction.guild.icon else None
        )

        embed.add_field(
            name="created on",
            value=(
                f"<t:{int(interaction.guild.created_at.timestamp())}:F> "
                f"(`{int(interaction.guild.created_at.timestamp())}`)"
            ),
            inline=True,
        )

        embed.add_field(
            name="members", value=str(interaction.guild.member_count), inline=True
        )

        embed.add_field(
            name="boosts",
            value=f"level {interaction.guild.premium_tier} ({interaction.guild.premium_subscription_count} boosts)",
            inline=True,
        )

        await interaction.followup.send(embed=embed)


async def setup(bot):
    await bot.add_cog(StatsCog(bot))
