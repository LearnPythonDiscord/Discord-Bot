import discord
import re
from discord.ext import commands


class submit_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def submit(self, ctx, *, args):
        if ctx.guild is None:
            pastebin_pattern = r'https:\/\/(?:pastebin|hastebin|gist).com\/.*'
            block_pattern = r'^(?:`{1,3}(?:python|py)?)([\s\S]*[^`{1,3}])(?:`{1,3})$'
            submission = re.search(pastebin_pattern, args, re.MULTILINE)
            if submission is None:
                submission = re.search(block_pattern,args, re.MULTILINE)
            if submission is None:
                await ctx.send('You must wrap your code with \`\`\`py and finish it with \`\`\` ')
            else:
                submission = submission.group(0)
                chan = self.bot.get_channel(731153486921728011)
                submit_embed = discord.Embed(
                    title='New submission', colour=0x00FA00)
                submit_embed.add_field(
                    name='Author', value=ctx.message.author, inline=False)
                submit_embed.add_field(
                    name='Code', value=f'```{submission}```', inline=False)
                await chan.send(embed=submit_embed)
                await ctx.send('Thank you for your submission')

        else:
            await ctx.send('This command can only be used in DMs')
            try:
                await ctx.author.send(f'Your message was deleted but here was the content. {ctx.message.content}')
            except:
                print('Couldnt dm this user')
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(submit_cog(bot))
