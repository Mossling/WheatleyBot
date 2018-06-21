
#Bot built by Noah, for Xander's Discord server

import discord
from discord.ext import commands
import asyncio
import chalk

#host config - None changable
token = "NDQ5NzA5NzEzOTE2MTY2MTQ0.Depjsg.PqAQCSS0ngFNKQvkCsWA3KiAKiE"
max_vote_delay = 5 # 5 seconds
min_vote_delay = 300 # 5*60 5 minutes

#config - changeable by vote
prefix = "!"
vote_delay = 10

bot = commands.Bot(command_prefix=prefix)

#Command to show config settings
@bot.command(pass_context=True, name="settings")
async def cmd_settings(ctx):
    await bot.say('Command prefix is '+prefix+'.')
    await bot.say('Voting timer is '+str(vote_delay)+' seconds.')

@bot.event
async def on_ready():
    print("Ready when you are!")

#@bot.event
#async def on_message(message):
#    print("The message's content was: " + message.content)


@bot.command(pass_context=True, name="ping")
async def cmd_ping(ctx):
    await bot.say("ponggggg!")

@bot.command(pass_context=True, name="echo")
async def cmd_echo(ctx, *, arg):
    await bot.say(arg)


async def run_reaction_vote(temp_mes, delay):
    # Add reactions for voting and wait
    await bot.add_reaction(temp_mes, "👍")
    await bot.add_reaction(temp_mes, "👎")
    print(delay)
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

@bot.group(pass_context=True, name="set")
async def grp_set(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("Improper use")

@grp_set.group(pass_context=True, name="server")
async def grp_server(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("Improper use")

@grp_server.command(pass_context=True, name="name")
async def cmd_name(ctx, new_name):
    server = ctx.message.author.server # get target server for name change

    if(new_name != server.name):

        temp_mes = await bot.say('Voting for new server name: "' +new_name+ '"')

        if await run_reaction_vote(temp_mes, vote_delay):
            await bot.say('Changing server name to: "' +new_name+ '"')
            await bot.edit_server(server, name=new_name)
        else:
            await bot.say("Vote failed")
    else:
        await bot.say("Current name and new name are the same")

@grp_set.group(pass_context=True, name="channel")
async def grp_channel(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("Improper use")

@grp_channel.command(pass_context=True, name="name")
async def cmd_name(ctx, target_channel_name, new_name):
    for channel in (ctx.message.author.server.channels):
        if channel.name == target_channel_name:
            target_channel = channel
            #TODO resolve two channels of the same name
    #TODO allow targeting by ID
    
    #TODO tell the user that capatalized letters are not used
    
    if(new_name != target_channel.name):
        
        temp_mes = await bot.say('Voting to change channel '+target_channel.name+'\'s name to: "' +new_name+ '"')
        
        if await run_reaction_vote(temp_mes, vote_delay):
            await bot.say('Changing name of channel '+target_channel.name+' to: "' +new_name+ '"')
            await bot.edit_channel(target_channel, name=new_name)
        else:
            await bot.say("Vote failed")
    else:
        await bot.say("Current name and new name are the same")

@grp_set.group(pass_context=True, name="config")
async def grp_config(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("Improper use")

#Command for setting the vote delay
@grp_config.command(pass_context=True, name="vote_delay")
async def cmd_vote_delay(ctx, arg1):
    global vote_delay
    if ((arg1) <= "600") and ((arg1) >= "10"):
        await bot.say('Changing vote delay to: ' +arg1+' seconds.')
        vote_delay = (int(arg1))
    
bot.run(token)
