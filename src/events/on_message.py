from discord.ext import commands


class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        content = message.content.lower()

        if content in ["brb", "be right back"]:
            await message.channel.send(
                "https://tenor.com/view/this-isnt-an-airport-no-gif-26083761"
            )
        elif content in ["im back", "i'm back"]:
            await message.channel.send(f"hi back, i'm {self.bot.user.name}")
        await self.bot.process_commands(message)


async def setup(bot):
    await bot.add_cog(OnMessageCog(bot))
