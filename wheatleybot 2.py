
#Bot built by Noah, for Xander's Discord server

import discord
from discord.ext import commands
import asyncio
import chalk

#config
token = "NDQ5NzA5NzEzOTE2MTY2MTQ0.Depjsg.PqAQCSS0ngFNKQvkCsWA3KiAKiE"
prefix = "!"
vote_delay = 5
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Ready when you are!")

#@bot.event
#async def on_message(message):
#    print("The message's content was: " + message.content)

    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("ponggggg!")
    await bot.say(str(ctx.message.channel))


@bot.command(pass_context=True)
async def echo(ctx, *, arg):
    await bot.say(arg)


async def run_reaction_vote(temp_mes, delay):
    # Add reactions for voting and wait
    await bot.add_reaction(temp_mes, "👍")
    await bot.add_reaction(temp_mes, "👎")
    await asyncio.sleep(delay)
    #await bot.say("waited " +str(vote_delay)+ " seconds") # temp message
        
    mes = discord.utils.get(bot.messages,id=temp_mes.id) # get long term message from cache
        
    # tally votes
    thumbs_ups = 0
    thumbs_downs = 0
    for react in mes.reactions:
        if react.emoji == "👍":
            thumbs_ups = react.count
        elif react.emoji == "👎":
            thumbs_downs = react.count
        #else: TODO remove any other emoji
    return thumbs_ups > thumbs_downs # returns true if success

@bot.command(pass_context=True)
async def servernamevote(ctx, arg):
    server = ctx.message.author.server # get target server for name change
    
    if(arg != server.name):
        
        temp_mes = await bot.say('Voting for new server name: "' +arg+ '"')
        
        if await run_reaction_vote(temp_mes, vote_delay):
            await bot.say('changing name to: "' +arg+ '"')
            await bot.edit_server(server, name=arg)
        else:
            await bot.say("Vote failed")
    else:
        await bot.say("Same as current name")



@bot.command(pass_context=True)
async def channelnamevote(ctx, arg1, arg2):
    for channel in (ctx.message.author.server.channels):
        if channel.name == arg1:
          target_channel = channel
    
    if(arg2 != target_channel.name):
        
        temp_mes = await bot.say('Voting for new channel '+arg1+' name: "' +arg2+ '"')
        
        if await run_reaction_vote(temp_mes, vote_delay):
            await bot.say('Changing name of '+arg1+' channel to: "' +arg2+ '"')
            await bot.edit_channel(target_channel, name=arg2)
        else:
            await bot.say("Vote failed")
    else:
        await bot.say("Same as current name")


bot.run(token)