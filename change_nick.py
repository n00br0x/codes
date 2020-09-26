import discord
from discord.ext import commands
class change_nick(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def change_nick(self, ctx, newnick): #here, the m:discord.Member not only instantises the class, but also accepts it as an argument
        m: discord.Member = ctx.message.author
        await ctx.message.delete(delay = 10.0)
        await m.edit(nick = newnick)
        a = await ctx.channel.send(f'your nickname has been changed to {newnick}')
        await a.delete(delay = 10.0)

        return
def setup(client):
    client.add_cog(change_nick(client))
