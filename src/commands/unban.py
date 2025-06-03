import discord
from discord import app_commands

async def setup(bot):
    @app_commands.command(name="unban", description="unbans a user by id")
    @app_commands.describe(user_id="the id of the user to unban")
    async def unban(interaction: discord.Interaction, user_id: str):
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("you don’t have permission to unban users.", ephemeral=True)
            return

        try:
            user = await bot.fetch_user(int(user_id))
            await interaction.guild.unban(user)
            await interaction.response.send_message(f"✅ unbanned `{user}`")
        except discord.NotFound:
            await interaction.response.send_message("user not found or not banned.", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("i don’t have permission to unban that user.", ephemeral=True)
        except ValueError:
            await interaction.response.send_message("invalid user id.", ephemeral=True)

    @app_commands.command(name="banned", description="shows list of banned users")
    async def banned(interaction: discord.Interaction):
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("you don’t have permission to view bans.", ephemeral=True)
            return

        bans = await interaction.guild.bans()

        if not bans:
            await interaction.response.send_message("🚫 no banned users.")
            return

        desc = "\n".join([f"`{entry.user.id}` - {entry.user}" for entry in bans[:20]])
        if len(bans) > 20:
            desc += f"\n...and {len(bans) - 20} more"

        embed = discord.Embed(
            title=f"🔒 banned users in {interaction.guild.name}",
            description=desc,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    bot.tree.add_command(unban)
    bot.tree.add_command(banned)
