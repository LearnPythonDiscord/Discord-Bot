import discord
import json
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='lp!')

cogs_to_load = ['cogs.event_cog',
                'cogs.hello_world',
                'cogs.submit_cog',
                'cogs.how_to_cog',
                'cogs.latex_parser_cog',
                'cogs.help_cog']

if __name__ == "__main__":
    for extension in cogs_to_load:
        bot.load_extension(extension)
        print(f'{extension} loaded')

bot.run(os.getenv('BOT_TOKEN'))
