import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

print(TOKEN)