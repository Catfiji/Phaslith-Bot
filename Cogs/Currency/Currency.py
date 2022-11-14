import asyncio

from discord.ext import commands
from discord.ext.commands import MissingRole
from Cogs.Currency.CurrencyFunctions.currency_functions import *

#;---------------------------------------------------------------------------

class Currency(commands.Cog):
    def __init__(self, client):
        self.client = client

    #;- Balance command
    @commands.command(aliases=["balance"])
    @commands.has_role("Player")
    async def bal(self, ctx):
        try:
            await ctx.reply(f"Balance: {get_user_wallet(ctx.author.id)}", delete_after=5.0)
            await asyncio.sleep(5.0)
            await ctx.message.delete()
        except Exception as e:
            print(e)

    @bal.error
    async def bal_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("You need to setup your profile!", delete_after=3.0)

    #;- Deposit command
    @commands.command(aliases=["deposit", "depo"])
    @commands.has_role("Player")
    async def dep(self, ctx, amount):
        try:
            amount = int(amount)
            deposit(ctx.author.id, amount)
            await ctx.reply(f"*Deposited* {amount}", delete_after=5.0)
            await asyncio.sleep(5.0)
            await ctx.message.delete()

        except Exception as e:
            print(e)

    @dep.error
    async def dep_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("You need to setup your profile!", delete_after=3.0)

    #;- Withdrawl command
    @commands.command(aliases=["withdrawl", "with"])
    @commands.has_role("Player")
    async def withdraw(self, ctx, amount):
        try:
            amount = int(amount)
            withdrawl(ctx.author.id, amount)
            await ctx.send(f"{ctx.author.mention} *Withdrew* {amount}", delete_after=5.0)
            await asyncio.sleep(5.0)
            await ctx.message.delete()

        except Exception as e:
            print(e)

    @withdraw.error
    async def withdraw_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("You need to setup your profile!", delete_after=3.0)


#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(Currency(client))