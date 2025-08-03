import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

celal = commands.Bot(command_prefix='$', intents=intents)

@celal.event
async def on_ready():
    print(f'{celal.user} olarak giriş yaptık')

@celal.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {celal.user}, bir Discord sohbet botuyum!')

@celal.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@celal.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

celal.run("TOKEN")