import asyncio

from discord.ext import commands
import discord
from discord.ext.commands import MissingRole
from Cogs.User.SetupFunctions import setup_player
from Cogs.Currency.CurrencyFunctions.currency_functions import get_user_wallet, get_user_bank
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
    async def profile(self, ctx, member: discord.Member = None):
        # TODO:
        if member == None:
            member = ctx.author
        name = member.display_name
        avatar = member.display_avatar

        profile_embed = discord.Embed(title=f"{name}'s profile", description="",
                                      color=discord.Color.random())
        profile_embed.add_field(name="Balance", value=f"${get_user_wallet(ctx.author.id)}", inline=True)
        profile_embed.add_field(name="Bank", value=f"${get_user_bank(ctx.author.id)}", inline=True)

        await ctx.send(embed=profile_embed, delete_after=10.0)
        await asyncio.sleep(5.0)
        await ctx.message.delete()

    @profile.error
    async def profile_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("do !setup to setup your profile!", delete_after=3.0)

#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(User(client))