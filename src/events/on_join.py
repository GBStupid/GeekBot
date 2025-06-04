from discord.ext import commands
import discord

class OnJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = 1259848364564938815  
        channel = member.guild.get_channel(channel_id)
        if channel:
            await channel.send(f"Welcome to the server, {member.mention}! :HYPED:")

async def setup(bot):
    await bot.add_cog(OnJoinCog(bot))
