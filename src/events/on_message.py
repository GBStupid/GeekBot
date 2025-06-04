import json
import re

from discord.ext import commands


class OnMessageCog(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        content = message.content.lower()

        for rule in self.config:
            if re.search(rule["match"], content):
                response = rule["response"].format(
                    user_name=self.bot.user.name,
                    author_name=message.author.name,
                    content=content,
                )
                if response:
                    await message.channel.send(response)

                break

        await self.bot.process_commands(message)


async def setup(bot):
    with open("config/auto_respond.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    await bot.add_cog(OnMessageCog(bot, config))
