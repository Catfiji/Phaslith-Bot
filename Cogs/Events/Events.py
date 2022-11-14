import asyncio
from discord.ext import commands
import discord

#;---------------------------------------------------------------------------

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    # on ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("-" * 14)
        print("client is online")
        await self.client.change_presence(status=discord.Status.dnd, activity=discord.Game('Testing'))

    # member join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        await channel.send(f"Welcome {member.mention} to the server.", delete_after=30.0)

    # member leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        await channel.send(f"{member.mention} has left the server.", delete_after=30.0)

async def setup(client):
    await client.add_cog(Events(client))