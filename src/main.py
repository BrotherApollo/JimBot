import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Local Imports
from timecard import summarize_payperiod

# Loading discord token form environement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setting up logging
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

# Manging discord bot permissions
intents = discord.Intents.default()
intents.message_content = True
# intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


# !timecard
@bot.command()
async def timecard(ctx):
    await ctx.send(summarize_payperiod())

bot.run(token=TOKEN, log_handler=handler, log_level=logging.DEBUG)