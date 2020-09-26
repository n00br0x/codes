import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

changers = {"board_member" : 0, "GOD" : 1}
class change_nickname(commands.Cog):
    def __init__(self,client):
        self.client = client
    @has_permissions(manage_nicknames = True)
    @commands.command()
    async def change_nickname(self, ctx, m:discord.Member, newnick): #here, the m:discord.Member not only instantises the class, but also accepts it as an argument
        flag = 0
        for y in ctx.message.author.roles:
            if y.name in changers:
                flag = 1
                await ctx.message.delete(delay = 10.0)
                await m.edit(nick = newnick)
                a = await ctx.channel.send(f'{m}s nickname has been changed to {newnick}')
                await a.delete(delay = 10.0)
                await ctx.message.delete(delay = 10.0)
                return
        if flag == 0:
            a = await ctx.channel.send(f'you do not have permissions to do so, contact a higher up')
            await a.delete(delay = 10.0)
            await ctx.message.delete(delay = 10.0)
    @change_nickname.error
    async def nickname_error(self,ctx,error):
        if isinstance(error, commands.BadArgument):
            a = await ctx.channel.send(f'Member not found try again')
            await a.delete(delay = 10.0)
            await ctx.message.delete(delay = 10.0)
        if isinstance(error, Checkfailure):
            a = await ctx.channel.send(f'You dont have required permissions for this, contact a higher up')
            await a.delete(delay = 10.0)
            await ctx.message.delete(delay =  10.0)
def setup(client):
    client.add_cog(change_nickname(client))
