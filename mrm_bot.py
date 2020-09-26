import os
import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get('DISCORD_TOKEN')
bot = commands.Bot(command_prefix = '!')
#roles and ids
d = discord.Guild
commmands_channel = 749517534897766471
gen_channel = 745983898839679039
tp = 749580263733985332
tm = 749579586966126663
bm = 749579859755401237
tm_verify = 749663259262582794
bm_verify = 749663323691155526
eve = 745983898839679036
alm_verify = 752403301705842759
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        a = await ctx.channel.send(f'command not found')
        await a.delete(delay = 10.0)
        await ctx.message.delete(delay = 10.0)
    else:
        a = await ctx.channel.send(f'error')
        await a.delete(delay = 10.0)
        await ctx.message.delete(delay = 10.0)

@bot.event
## shows that bot is ready
async def on_ready():
    print ('Bot is ready')
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#white_check_mark = ✅
#no_entry_sign = 🚫
@bot.event
async def on_member_join(member): ## when a member joins
    print(f'{member} has joined a server') ## prints in the run window
    id = member.id ## gets user id of person who just joined
    print(f'member id: {id}') ## print member id in run window

    user_dm = bot.get_user(id)
    await user_dm.send(f'Hello {member} please read the rules section of this server please head over to verifying your role after reading the rules')
    role = member.guild.get_role(role_id = tp)#getting tp role
    print(f'role obtained role id: {role.id}, role name: {role.name}')
    await member.add_roles(role)
    await user_dm.send(f'hello, your current role is {role}, head over to verify-roles to verify/change your role')
    ##await gen_channel.send(f'Hello {member} please read the rules section to get started')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        #print('user x')#checks if message was from bot, to prevent it from going into a loop
        return

    if message.content.startswith('hello'):
        await message.channel.send(f'Hello!')
    await bot.process_commands(message)


bot.run(token)
