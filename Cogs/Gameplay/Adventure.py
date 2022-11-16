import random

import discord
from discord.ext import commands
from discord.ext.commands import MissingRole
from Cogs.User.LevelingFunctions.leveling import get_user_level, get_user_exp
from Cogs.Currency.CurrencyFunctions.currency_functions import get_user_wallet
from Cogs.Gameplay.AdventureFunctions.LocationFunctions import get_user_location_id, get_location_information
#;---------------------------------------------------------------------------

class Adventure(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["walk"])
    @commands.has_role("Player")
    async def step(self, ctx):
        try:
            location_info = get_location_information(get_user_location_id(ctx.author.id))
            print(location_info[2])
            gold = random.randint(location_info[3],location_info[4])
            exp = random.randint(location_info[5], location_info[6])
            print(gold)
            print(exp)
        except Exception as e:
            print(e)

    @step.error
    async def step_error(self, error, ctx):
        if isinstance(error, MissingRole):
            await ctx.send("you need to setup your profile!", delete_after=3.0)

#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(Adventure(client))