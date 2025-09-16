import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {client.user}, bir Discord sohbet botuyum!')

client.run("TOKEN")
