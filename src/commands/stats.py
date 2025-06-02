import discord
from discord import app_commands

async def setup(bot):
    @app_commands.command(name="serverstats", description="shows server stats")
    async def serverstats(interaction: discord.Interaction):
        guild = interaction.guild


        embed = discord.Embed(
            title=f"📊 server stats for {guild.name}",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=guild.icon.url if guild.icon else discord.Embed.Empty)


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

    bot.tree.add_command(serverstats)
