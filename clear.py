import discord
from discord.ext import commands
clearers = {"board_member" : 0, "GOD" : 1}
class clear(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount = 5):
        m:discord.Member = ctx.message.author
        if m.name not in clearers:
            await ctx.channel.purge(limit = amount)
            print(f'clearing')
        else:
            a = await ctx.channel.send(f'You do not have permission to do this, contact a board_member or GOD')
            await a.delete(delay = 10.0)
    @commands.command()
    async def bulk_clear(self, ctx, amount = 100):
        m:discord.Member = ctx.message.author
        if m.name not in clearers:
            await ctx.channel.purge(limit = amount)
            print(f'bulk clearing')
        else:
            a = await ctx.channel.send(f'You do not have permission to do this, contact a board_member or GOD')
            await a.delete(delay = 10.0)



def setup(client):
    client.add_cog(clear(client))
