import discord

async def setup(bot):
    @bot.event
    async def on_ready():
        print(f"✅ Logged in as {bot.user}")
        try:
            synced = await bot.tree.sync()
            print(f"🔁 Synced {len(synced)} commands globally.")
        except Exception as e:
            print(f"❌ Failed to sync commands: {e}")
