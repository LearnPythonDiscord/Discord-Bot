import discord
import json
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='lp!')

cogs_to_load = ['cogs.event_cog',
                'cogs.hello_world',
                'cogs.submit_cog']

if __name__ == "__main__":
    for extension in cogs_to_load:
        bot.load_extension(extension)
        print(f'{extension} loaded')

bot.run(os.environ['BOT_TOKEN'])
