import discord, random, json
from discord.ext import commands, tasks

class event_cogs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('The bot is up and running')  

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Hey there! Welcome to `learn python discord`. Courses are every tuesday, in between these days we have challenges running, which you can see in the #challenges channel. We have a custom bot (this one) us `lp!help` to see what you can do')
def setup(bot):
    bot.add_cog(event_cogs(bot))
