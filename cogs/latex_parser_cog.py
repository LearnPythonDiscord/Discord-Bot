import discord
import os
from discord.ext import commands
import matplotlib.pyplot as plt                                                 
import sympy       
class latex_parser(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def latex(self,ctx,*,args):                                                             
        try:           
            lat = sympy.latex(args)                                                            
            plt.text(0, 0.6, r"$%s$" % lat, fontsize = 20)                                  
            fig = plt.gca()                                                                 
            fig.axes.get_xaxis().set_visible(False)                                         
            fig.axes.get_yaxis().set_visible(False)                                         
            plt.savefig('out') #or savefig                                                          
            await ctx.send(file=discord.File('out.png'))
            return
        except ValueError:
            await ctx.send('Invalid latex')
            return
        await ctx.send('uhm, something has gone wrong') # will only get here if the program hasnt already returned
        

def setup(bot):
    bot.add_cog(latex_parser(bot))