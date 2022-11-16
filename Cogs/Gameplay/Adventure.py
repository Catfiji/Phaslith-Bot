import asyncio
import random

import discord
from discord.ext import commands
from discord.ext.commands import MissingRole
from Cogs.User.LevelingFunctions.leveling import get_user_level, get_user_exp, add_exp
from Cogs.Currency.CurrencyFunctions.currency_functions import get_user_wallet, add_wallet_bal
from Cogs.Gameplay.AdventureFunctions.LocationFunctions import get_user_location_id, get_location_information
#;---------------------------------------------------------------------------

class Adventure(commands.Cog):
    def __init__(self, client):
        self.client = client

    #;- Step command
    @commands.command(aliases=["walk", "adventure"])
    @commands.has_role("Player")
    async def step(self, ctx):
        try:
            user_id = ctx.author.id
            location_info = get_location_information(get_user_location_id(user_id))

            gold = random.randint(location_info[3], location_info[4])
            exp = random.randint(location_info[5], location_info[6])

            add_wallet_bal(user_id, gold)
            add_exp(user_id, exp)

            step_embed = discord.Embed(title=f"[debug] Adventure", description="You take a step forward",color=discord.Color.random())
            step_embed.add_field(name="Rewards", value=f"+${gold}\n+{exp}xp", inline=True)

            await ctx.reply(embed=step_embed, delete_after=3.0)
            await asyncio.sleep(5.0)
            await ctx.message.delete()
        except Exception as e:
            print("[Phaslith] " + str(e))

    @step.error
    async def step_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("you need to setup your profile!", delete_after=3.0)

#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(Adventure(client))