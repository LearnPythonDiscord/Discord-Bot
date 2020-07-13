import discord
from discord.ext import commands
from textwrap import dedent
"""
!code that explains how to paste code in Discord with proper markdown.
!paste that explains how to paste code on something like GitHub Gist for larger files.
"""
class how_to_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=['md','markup','howtosend'])
    async def code(self,ctx):
        code_embed = discord.Embed(title='How to send code properly',colour=0xF0FAAF)
        code_embed.add_field(name='How to send underlined things?',
                            value='To underline things you use double underscore \_\_Like this\_\_ and it should result in something like __this__',
                            inline=False)
        code_embed.add_field(name='How to highlight code',
                            value='To highlight your code like `this` you need to use backticks, so do something like \`this\` which will result in `this`',
                            inline=False)
        code_embed.add_field(name='Code blocks',
                            value=dedent('''Code blocks are what you should be using with your code, if possible. To do these you use three backticks \`\`\`\n
                            your code here
                            \`\`\`
                            It should result in something like this:
                            ```\nprint("hello world")\n```
                            '''),
                            inline=False) 
        code_embed.add_field(name='Python code blocks',
                            value='''The exact same as normal ones however after your backticks you must put py, so like this : \`\`\`py
                                    Which will result in something like this:
                                    ```py\nprint("hello world")```''',
                            inline=False)
        code_embed.add_field(name='Does your code exceed 2k characters?',
                            value='''If your code exceeds 2k characters then discord will not allow you to send the code. To bypass this you can use sites such as
                                    pastebin/hastebin/github gists. Simply paste your code into one of these sites and share the link. Sharing the files is not a good
                                    idea as it makes some people suspicious as to whether it is malicious or not''',
                            inline=False)
        
        await ctx.send(embed=code_embed)

def setup(bot):
    bot.add_cog(how_to_cog(bot))