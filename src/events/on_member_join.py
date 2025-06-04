import json
import os
import discord
from discord.ext import commands


class MemberJoinCog(commands.Cog):
    def __init__(self, bot: commands.Bot, config):
        self.bot = bot
        self.config = config

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not self.config:
            return

        guild = member.guild

        guild_config = self.config[guild.id]
        if not guild_config:
            return

        channel = guild.system_channel
        if guild_config["default_channel"]:
            channel = self.bot.get_channel(guild_config["default_channel"])

        if not channel or not isinstance(channel, discord.TextChannel):
            return

        await channel.send(
            guild_config["join_message"].format(
                member_name=member.display_name, member_count=guild.member_count
            )
        )


async def setup(bot: commands.Bot):
    config = None
    config_file = "config/member_join.json"
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        print("⚠️  WARN: member_join.json does not exist, disabling welcome messages.")

    await bot.add_cog(MemberJoinCog(bot, config))
