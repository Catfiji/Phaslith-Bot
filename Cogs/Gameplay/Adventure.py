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

    @commands.command(aliases=["walk"])
    @commands.has_role("Player")
    async def step(self, ctx):
        user_id = ctx.author.id
        try:
            location_info = get_location_information(get_user_location_id(user_id))
            user_wallet = get_user_wallet(user_id)
            user_exp = get_user_exp(user_id)
            gold = random.randint(location_info[3],location_info[4])
            exp = random.randint(location_info[5], location_info[6])
            add_wallet_bal(user_id, gold)
            add_exp(user_id, exp)
            await ctx.reply(f"[debug] +${gold}, +{exp}xp")
        except Exception as e:
            print("[Phaslith] " + e)

    @step.error
    async def step_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("you need to setup your profile!", delete_after=3.0)

#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(Adventure(client))