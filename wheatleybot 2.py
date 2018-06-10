#Bot built by Noah, for Xander's Discord server

import discord
from discord.ext import commands
import asyncio
#import chalk

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Ready when you are!")

@bot.event
async def on_message(message):
    print("The message's content was: " + message.content)
    await bot.process_commands(message)

    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("ponggggg!")
    #await bot.say(str(ctx.message.channel))



@bot.command(pass_context=True)
async def echo(ctx, *, arg):
    await bot.say(arg)


@bot.command(pass_context=True)
async def channelnamevote(ctx, arg):
    mes = await bot.say('Voting for new server name: "' +arg +'"')
    await bot.add_reaction(mes, "👍")
    await bot.add_reaction(mes, "👎")



bot.run("NDQ5NzA5NzEzOTE2MTY2MTQ0.Depjsg.PqAQCSS0ngFNKQvkCsWA3KiAKiE")
