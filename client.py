import asyncio
import config
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all(), help_command=None)
#;---------------------------------------------------------------------------

#;- load cogs
async def load_cogs():
    cogs_loaded = 0 # Slice of Life
    cogs = [
        "Cogs.Utilities.Utilities",
        "Cogs.Admin.Admin",
        "Cogs.User.User",
        "Cogs.Currency.Currency",
        "Cogs.Events.Events",
        "Cogs.Gameplay.Adventure"
    ]
    for i in cogs:
        try:
            await client.load_extension(i) # load each cog in cogs list
            cogs_loaded += 1
        except Exception as e:
            print(f"[Phaslith] {e}\n Problem loading '{i}'") # Uh Oh! Error

    print(f"[Phaslith] I have loaded {cogs_loaded} cog/s")

#;- main
async def main():
    await load_cogs()
    await client.start(config.TOKEN)

#;---------------------------------------------------------------------------
if __name__ == '__main__':
    asyncio.run(main())