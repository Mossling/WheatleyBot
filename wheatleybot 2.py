
#Bot built by Noah, for Xander's Discord server

import discord
from discord.ext import commands
import asyncio
import chalk

import config_manager

config_manager.load_config()

p = config_manager.Config.get_value("prefix")
bot = commands.Bot(command_prefix=p)

#Command to show config settings
@bot.command(pass_context=True, name="settings")
async def cmd_settings(ctx):
    p = config_manager.Config.get_value("prefix")
    vd = config_manager.Config.get_value("vote_delay")
    await bot.say('Command prefix is ' +p+ '.')
    await bot.say('Voting timer is ' +str(vd)+ ' seconds.')

@bot.event
async def on_ready():
    print("Ready when you are!")

@bot.command(pass_context=True, name="shutdown")
async def cmd_shutdown(ctx):
    config_manager.save_config()
    await bot.close()
#@bot.event
#async def on_message(message):
#    print("The message's content was: " + message.content)


@bot.command(pass_context=True, name="ping")
async def cmd_ping(ctx):
    await bot.say("ponggggg!")

@bot.command(pass_context=True, name="echo")
async def cmd_echo(ctx, *, text):
    await bot.say(text)


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

        vd = config_manager.Config.get_value("vote_delay")

        if await run_reaction_vote(temp_mes, vd):
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
        
        vd = config_manager.Config.get_value("vote_delay")

        if await run_reaction_vote(temp_mes, vd):
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
async def cmd_vote_delay(ctx, new_vote_delay):
    max_vd = config_manager.Config.get_value("max_vote_delay")
    min_vd = config_manager.Config.get_value("min_vote_delay")
    old_vd = config_manager.Config.get_value("vote_delay")
    new_vd = int(new_vote_delay)


    if old_vd != new_vd:
        if new_vd <= max_vd and new_vd >= min_vd:
            temp_mes = await bot.say('Voting to change vote delay to: ' +new_vote_delay+ ' seconds.')
            if await run_reaction_vote(temp_mes, old_vd):
                await bot.say('Changing vote delay to: ' +new_vote_delay+ ' seconds.')
                config_manager.Config.set_value("vote_delay", new_vd)
            else:
                await bot.say("Vote failed")
        else:
            await bot.say('Invalid vote delay. Delay must be between ' +str(min_vd)+ ' and ' +str(max_vd)+ ' seconds.')
    else:
        await bot.say('New vote delay is the same as current vote delay.')
t = config_manager.Config.get_value("token")
bot.run(t)
