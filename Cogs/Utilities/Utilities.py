from discord.ext import commands
#;---------------------------------------------------------------------------

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    #;- Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"**My ping** : {round(self.client.latency) * 1000}ms", delete_after=10.0)

#;---------------------------------------------------------------------------
async def setup(client):
    await client.add_cog(Utilities(client))