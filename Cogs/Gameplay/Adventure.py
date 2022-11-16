import random

import discord
from discord.ext import commands
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
            chance_for_enemy = int(get_location_information(get_user_location_id(ctx.author.id))[2])
            gold_range_min = get_location_information(get_user_location_id(ctx.author.id))[3]
            gold_range_max = get_location_information(get_user_location_id(ctx.author.id))[4]
            print(chance_for_enemy)
            gold = random.randint(gold_range_min,gold_range_max)
            print(gold)
        except Exception as e:
            print(e)

async def setup(client):
    await client.add_cog(Adventure(client))