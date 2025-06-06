import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

log_channel_id = None  # dynamically set via /log command

async def setup(bot):
    @app_commands.command(name="log", description="set the channel where events will be logged")
    @app_commands.describe(channel="channel to log events in")
    async def log(interaction: discord.Interaction, channel: discord.TextChannel):
        global log_channel_id
        log_channel_id = channel.id
        await interaction.response.send_message(f"✅ logging channel set to {channel.mention}", ephemeral=True)

    async def send_log(bot, guild: discord.Guild, embed: discord.Embed):
        if log_channel_id is None:
            return
        channel = guild.get_channel(log_channel_id)
        if isinstance(channel, discord.TextChannel):
            await channel.send(embed=embed)

    @bot.event
    async def on_message_edit(before, after):
        if before.author.bot:
            return
        embed = discord.Embed(title="✏️ Message Edited", color=discord.Color.orange(), timestamp=datetime.utcnow())
        embed.set_author(name=str(before.author), icon_url=before.author.display_avatar.url)
        embed.add_field(name="Before", value=before.content[:1024] or "[no content]", inline=False)
        embed.add_field(name="After", value=after.content[:1024] or "[no content]", inline=False)
        embed.add_field(name="Channel", value=before.channel.mention)
        await send_log(bot, before.guild, embed)

    @bot.event
    async def on_message_delete(message):
        if message.author.bot:
            return
        embed = discord.Embed(title="🗑️ Message Deleted", color=discord.Color.red(), timestamp=datetime.utcnow())
        embed.set_author(name=str(message.author), icon_url=message.author.display_avatar.url)
        embed.add_field(name="Content", value=message.content[:1024] or "[no content]", inline=False)
        embed.add_field(name="Channel", value=message.channel.mention)
        await send_log(bot, message.guild, embed)

    @bot.event
    async def on_member_join(member):
        logger.info(f"{member} joined {member.guild.name}")
        embed = discord.Embed(title="📥 Member Joined", color=discord.Color.green(), timestamp=datetime.utcnow())
        embed.set_author(name=str(member), icon_url=member.display_avatar.url)
        embed.add_field(name="Account Created", value=f"<t:{int(member.created_at.timestamp())}:F>", inline=False)
        embed.add_field(name="Joined Server", value=f"<t:{int(member.joined_at.timestamp())}:F>", inline=False)
        await send_log(bot, member.guild, embed)

    @bot.event
    async def on_member_remove(member):
        logger.info(f"{member} left {member.guild.name}")
        embed = discord.Embed(title="📤 Member Left", color=discord.Color.red(), timestamp=datetime.utcnow())
        embed.set_author(name=str(member), icon_url=member.display_avatar.url)
        embed.add_field(name="Account Created", value=f"<t:{int(member.created_at.timestamp())}:F>", inline=False)
        await send_log(bot, member.guild, embed)

    @bot.event
    async def on_member_update(before, after):
        if before.bot:
            return

        if before.roles != after.roles:
            removed_roles = [role.mention for role in before.roles if role not in after.roles]
            added_roles = [role.mention for role in after.roles if role not in before.roles]
            embed = discord.Embed(title="🔧 Role Changes", color=discord.Color.blurple(), timestamp=datetime.utcnow())
            embed.set_author(name=str(after), icon_url=after.display_avatar.url)
            if added_roles:
                embed.add_field(name="Roles Added", value=", ".join(added_roles), inline=False)
            if removed_roles:
                embed.add_field(name="Roles Removed", value=", ".join(removed_roles), inline=False)
            await send_log(bot, after.guild, embed)

        if before.nick != after.nick:
            embed = discord.Embed(title="📝 Nickname Changed", color=discord.Color.teal(), timestamp=datetime.utcnow())
            embed.set_author(name=str(after), icon_url=after.display_avatar.url)
            embed.add_field(name="Before", value=before.nick or "None", inline=True)
            embed.add_field(name="After", value=after.nick or "None", inline=True)
            await send_log(bot, after.guild, embed)

    bot.tree.add_command(log)
