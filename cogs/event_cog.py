import discord, random, json
from discord.ext import commands, tasks

class event_cogs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('The bot is up and running')  

def setup(bot):
    bot.add_cog(event_cogs(bot))