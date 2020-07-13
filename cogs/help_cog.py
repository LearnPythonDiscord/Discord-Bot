import discord
import random
from discord.ext import commands
class help_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot.remove_command('help')
    
    @commands.command()
    async def help(self,ctx):
        help_embed = discord.Embed(title='Help',colour=random.randint(0,0xFFFFFF))
        help_embed.add_field(name='lp!code',value='''Aliases = lp!md, lp!markup, lp!howtosend
                                    This command tells you how to format your code
                                    Can be used: Anywhere''',
                            inline=False)
        help_embed.add_field(name='lp!latex',value='''Aliases = None
                                    Intepret latex into images (do not use *display style*) Command in early stages so might be a bit buggy)
                                    Can be used: Anywhere''',
                            inline=False)
        help_embed.add_field(name='lp!submit', value='''Aliases = None
                                    Submit your code to be reviewed
                                    Can be used: DM Only''',
                            inline=False)
        await ctx.send(embed=help_embed)

def setup(bot):
    bot.add_cog(help_cog(bot))