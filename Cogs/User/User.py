from discord.ext import commands
import discord
from Cogs.User.SetupFunctions import setup_player

#;---------------------------------------------------------------------------

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    #;- Setup command
    @commands.command(name="setup")
    async def setup(self,ctx):
        if setup_player.setup_player(ctx.author.id):
            member = ctx.author
            role = discord.utils.get(member.guild.roles, name="Player")
            await member.add_roles(role)
            await ctx.send("**Created user**")
        else:
            await ctx.send("**You already exist in the database!**")

    @commands.command(name="profile")
    @commands.has_role("Player")
    async def profile(self, ctx):
        # TODO:
        await ctx.send("profile")

#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(User(client))