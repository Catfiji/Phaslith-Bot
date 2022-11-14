from discord.ext import commands
from discord.ext.commands import MissingPermissions
import discord
#;---------------------------------------------------------------------------

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    #;- Purge command
    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit):
        limit = int(limit)
        await ctx.channel.purge(limit=limit)

    @purge.error
    async def purge_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!", delete_after=10.0)

    #;- Kick command
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if reason is None:
            reason = "No reason provided"
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f"User: {member.mention} has been kicked for '{reason}'", delete_after=10.0)

    @kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("You dont have permission to do that!", delete_after=10.0)

    #;- Ban Command
    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if reason is None:
            reason = "No reason provided"
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"User: {member.mention} has been banned for '{reason}'", delete_after=10.0)

    @ban.error
    async def ban_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("You dont have permission to do that!", delete_after=10.0)

    #;- Unban command
    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.User, *, reason=None):
        if reason is None:
            reason = f"No Reason Provided"
        await ctx.guild.unban(member, reason=reason)
        await ctx.send(f"{member.mention} has been **unbanned**", delete_after=10.0)

    @unban.error
    async def unban_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("You dont have permission to do that!", delete_after=10.0)



#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(Admin(client))