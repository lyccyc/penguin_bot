import discord
from discord.ext import commands

bot = commands.Bot(command_preFix="/")


@bot.event
async def on_ready():
    print("Bot is online!")


bot.run("MTE3MjEzMTAzNDM5NDAwMTQ3OA.Gwwtcw.cngLsPNDoGTsnVB0GRBuBk3FdDhtn6RxCDOTJU")
