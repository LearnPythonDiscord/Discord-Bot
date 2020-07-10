import discord
from discord.ext import commands
class hello_world_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def hello_world(self,ctx):
        await ctx.send(f'Hey there {ctx.message.author.mention}')


def setup(bot):
    bot.add_cog(hello_world_cog(bot))