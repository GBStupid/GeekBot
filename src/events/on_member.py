from enum import Enum
import json
import logging
import os
import discord
from discord.ext import commands


class EventType(Enum):
    JOIN = "join_message"
    LEAVE = "leave_message"


class WelcomeCog(commands.Cog):
    def __init__(self, bot: commands.Bot, logger: logging.Logger, config: dict):
        self.bot = bot
        self.logger = logger
        self.config = config

    def get_handler_payload(self, member: discord.Member, event_type: EventType):
        guild_config = self.config[member.guild.id]
        if not guild_config or not all(
            key in guild_config
            for key in ["default_channel", "join_message", "leave_message"]
        ):
            return None, None

        channel = (
            self.bot.get_channel(guild_config.get("default_channel"))
            or member.guild.system_channel
        )

        if not isinstance(channel, discord.TextChannel):
            return None, None

        message = guild_config[event_type].format(
            member_name=member.display_name, member_count=member.guild.member_count
        )

        return channel, message

    async def handle_member_event(self, member: discord.Member, event_type: EventType):
        if not self.config or not member:
            return

        channel, message = self.get_handler_payload(member, event_type)

        if not channel:
            return

        try:
            await channel.send(message)
        except KeyError as e:
            self.logger.warning(f"Missing placeholder in {event_type.value}: {e}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await self.handle_member_event(member, EventType.JOIN)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        await self.handle_member_event(member, EventType.LEAVE)


async def setup(bot: commands.Bot):
    logger = logging.getLogger(__name__)
    config = {}
    config_file = "config/welcome.json"
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        logger.warning(f"{config_file} does not exist, disabling welcome messages.")

    await bot.add_cog(WelcomeCog(bot, logger, config))
