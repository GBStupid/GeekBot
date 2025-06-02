import discord
from discord import app_commands
from discord.ext import commands


class StatsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverstats", description="shows server stats")
    async def serverstats(self, interaction: discord.Interaction):
        guild = interaction.guild

        if not guild:
            raise ValueError("Guild cannot be None")

        embed = discord.Embed(
            title=f"📊 server stats for {guild.name}",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)


        embed.add_field(
            name="created on",
            value=f"<t:{int(guild.created_at.timestamp())}:F> (`{int(guild.created_at.timestamp())}`)",
            inline=True
        )

        embed.add_field(name="members", value=str(guild.member_count), inline=True)

        embed.add_field(
            name="boosts",
            value=f"level {guild.premium_tier} ({guild.premium_subscription_count} boosts)",
            inline=True
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(StatsCog(bot))
