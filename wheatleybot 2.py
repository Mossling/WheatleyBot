#Bot built by Noah, for Xander's Discord server

import discord
from discord.ext import commands
import asyncio
import chalk

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Ready when you are!")

@bot.event
async def on_message(message):
    print("The message's content was: " + message.content)

@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)



@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


@bot.command()
async def channelnamevote(ctx.message)
    await 



bot.run("NDQ5NzA5NzEzOTE2MTY2MTQ0.Depjsg.PqAQCSS0ngFNKQvkCsWA3KiAKiE")
