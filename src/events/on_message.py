async def setup(bot):
    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        content = message.content.lower()

        if content in ["brb", "be right back"]:
            await message.channel.send("this isn't an airport, you don't need to announce your departure :3")
        elif content in ["im back", "i'm back"]:
            await message.channel.send(f"hi back, i'm {bot.user.name}")
        await bot.process_commands(message)
