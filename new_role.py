import discord
from discord.ext import commands
import asyncio
commmands_channel = 749517534897766471
gen_channel = 745983898839679039
tp = 749580263733985332
tm = 749579586966126663
bm = 749579859755401237
tm_verify = 749663259262582794
bm_verify = 749663323691155526
eve = 745983898839679036
alm_verify = 752403301705842759
#substem verification channel id
elec = 751439996166209546
mech = 751440030811029605
sc = 751440069197561867
rsc = 751440108733071441
mgmt = 751440569657720832
#subsystem id
electronics = 751446883037085769
mechanical = 751446875768356986
science = 751446936082448455
research = 751446965182660730
management = 751446986737319989
#role ids:
Alumnus = 752400567099457538
subsystem_channel = {"electronics" : elec, "mechanical" : mech, "science" : sc, "research" : rsc, "management" : mgmt}

subsystem = {"electronics" : electronics, "mechanical" : mechanical, "science" : science, "research" : research, "management" : management}

role_hierarchy = {"@everyone": 0, "taskphase" : 1 , "team_member" : 2 , "board_member" : 3 , "Alumnus" : 4 , "GOD" : 5}

role_ids = {"@everyone" : eve, "taskphase" : tp, "team_member" : tm, "board_member" : bm, "Alumnus" : Alumnus}

role_verification = {"team_member" : tm_verify, "board_member" : bm_verify, "Alumnus" : alm_verify}

class new_role(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def new_role(self, ctx, r: discord.Role):
        msg_verify = "null"
        if (ctx.message.author == self.client.user):
            return

        m:discord.Member = ctx.message.author
        id = m.id
        user_dm = self.client.get_user(id)
        flag = 1
        for y in role_ids:
            if r.name == y:
                role = m.guild.get_role(role_id = role_ids.get(y))
                flag = 0
        if flag == 1:
            a = await user_dm.send(f'role not found, please try again')
            await ctx.channel.purge(limit = 1)
            await a.delete(delay = 10.0)
            return
        f_new_role = 1
        for a in m.roles:
            #print(f'looping')
            if r.name == a.name:
                id = m.id
                user_dm = self.client.get_user(id)
                a = await user_dm.send(f'you already have this role')
                await ctx.channel.purge(limit = 1)
                await a.delete(delay = 10.0)
                f_new_role = 0
        role1 = "null"
        if (f_new_role == 1):
            h = 1
            for xyz in m.roles:
                if(xyz.name in subsystem):
                    continue
                if(role_hierarchy.get(r.name) < role_hierarchy.get(xyz.name)):
                    role1 = xyz.name
                    h = 0
            if(h == 1):
                print(f'new role')
                #dictionary
                roles = role_verification
                for x in roles:
                    if r.name == x:
                        channel = self.client.get_channel(roles.get(x))
                msg_verify = await channel.send(f' {m} has requested to be {r}, allow? ')
                approve = "✅"
                deny = "🚫"
                await msg_verify.add_reaction(approve)
                await msg_verify.add_reaction(deny)
                x = await user_dm.send(f'your request has been sent')
                await x.delete(delay = 10.0)
            elif(h == 0):
                print(f'role denied;  reason: hierarchy ')
                a = await user_dm.send(f'you have a higher level role: " {role1} ", you cannot get the role: " {r} " ')
                await a.delete(delay = 10.0)
            await ctx.channel.purge(limit = 1)
        def check(payload):
            return payload.user_id != self.client.user.id and payload.message_id == msg_verify.id and str(payload.emoji) in ['✅', '🛑']

        try:
            payload = await self.client.wait_for('raw_reaction_add' , check=check, timeout = 180.0)
        except asyncio.TimeoutError:
            await ctx.send(f'The vote timed out. Please try again later.')
        else:
            if(str(payload.emoji) == '✅' ):
                id = m.id
                user_dm = self.client.get_user(id)
                #role = m.guild.get_role(role_id = tm)
                print(f'role obtained role id: {role.id}, role name: {role.name}')
                await m.add_roles(role)
                a = await user_dm.send(f'hello, your current role is {role}, head over to verify-roles to verify/change your role')
                await a.delete(delay = 10.0)
                for abc in m.roles:
                    if(abc.name in subsystem):
                        continue
                    if (role_hierarchy.get(r.name) > role_hierarchy.get(abc.name)):
                        if (abc.id == eve):
                            continue
                        else:
                            await m.remove_roles(abc)
                await msg_verify.delete(delay = 1.0)
                return
            elif(str(payload.emoji) == '🛑'):
                id = m.id
                user_dm = self.client.get_user(id)
                a = await user_dm.send(f'sorry your request was denied')
                await a.delete(delay = 10.0)
                print(f'denied')
                await msg_verify.delete(delay = 1.0)
                return
            else:
                return

def setup(client):
    client.add_cog(new_role(client))
