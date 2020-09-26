import discord
from discord.ext import commands
from discord.ext.commands import has_permissions,CheckFailure
clearers = {"board_member" : 0, "GOD" : 1}
class clear(commands.Cog):
    def __init__(self,client):
        self.client = client
    @has_permissions(manage_messages = True)
    @commands.command()
    async def clear(self, ctx, amount = 5):
        m:discord.Member = ctx.message.author
        print(f'clearing')
        await ctx.channel.purge(limit = amount)

    @commands.command()
    async def bulk_clear(self, ctx, amount = 100):
        m:discord.Member = ctx.message.author
        print(f'bulk clearing')
        await ctx.channel.purge(limit = amount)
    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error, CheckFailure):
            a = await ctx.channel.send(f'You do not have the permissions required ')
            await a.delete(delay = 10.0)
    @bulk_clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error, CheckFailure):
            a = await ctx.channel.send(f'You do not have the permissions required ')
            await a.delete(delay = 10.0)
def setup(client):
    client.add_cog(clear(client))
