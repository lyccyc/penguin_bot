import discord
import os
from discord.ext import commands

intents = discord.Intents.default()

os.environ[
    "TOKEN"
] = "MTE3MjEzMTAzNDM5NDAwMTQ3OA.GEoSqE.sWReG2mJIWPAPG83xmsPB5Mthvc6ciE3BOfqXU"

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print("Bot is online!")


TOKEN = os.environ["TOKEN"]

bot.run(TOKEN)
