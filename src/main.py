import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# Local Imports
from timecard import summarize_payperiod
from meme import random_meme
from excuses import generate_excuse

# Loading discord token form environement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN", "")
TIMECARD_CHANNEL =  int(os.getenv("TIMECARD_CHANNEL", 0))
TEST_CHANNEL =  int(os.getenv("TEST_CHANNEL", 0))
EMAIL_AID = os.getenv("EMAIL_AID", "")

# Scheduler
scheduler = AsyncIOScheduler()

# Setting up logging
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

# Manging discord bot permissions
intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=True)
intents.message_content = True
# intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    allowed_mentions=allowed_mentions
    )

# Commands

# !timecard
@bot.command()
async def timecard(ctx):
    """Responds to !timecard messages in the same channel"""
    await ctx.send(summarize_payperiod())
    
# !meme
@bot.command()
async def meme(ctx):
    filepath = random_meme()
    await ctx.send(file=discord.File(filepath))
    
# !excuse
@bot.command()
async def excuse(ctx):
    await ctx.send(generate_excuse())
    

# Scheduled Reminders

async def send_start_timecard_reminder():
    channel = bot.get_channel(TIMECARD_CHANNEL)
    await channel.send(f"")


async def send_timecard_reminder():
    """Post timecard reminders in a specific channel"""
    channel = bot.get_channel(TIMECARD_CHANNEL)
    await channel.send(summarize_payperiod())

# Test Reminders
async def send_test_reminder():
    channel = bot.get_channel(TEST_CHANNEL)
    await channel.send(summarize_payperiod())

@bot.event
async def on_ready():
    """Initilization, includes all schduled jobs"""
    if scheduler.running:
        return

    print(f"Logged in as {bot.user}")

    # Start your timecard reminder 
    scheduler.add_job(
        lambda: bot.loop.create_task(send_start_timecard_reminder()),
        CronTrigger(day="last", hour=18, minute=00)
        )
    scheduler.add_job(
        lambda: bot.loop.create_task(send_start_timecard_reminder()),
        CronTrigger(day=16, hour=18, minute=00)
        )

    # End of Month Timecard Reminder
    scheduler.add_job(
        lambda: bot.loop.create_task(send_timecard_reminder()),
        CronTrigger(day="last", hour=18, minute=00)
        )

    # Mid Month Timecard Reminder
    scheduler.add_job(
        lambda: bot.loop.create_task(send_timecard_reminder()),
        CronTrigger(day=15, hour=18, minute=00)
        )
    
    # Test
    scheduler.add_job(
        lambda: bot.loop.create_task(send_test_reminder()),
        CronTrigger(day=19, hour=13, minute=00)
        )
    
    scheduler.start()    

if __name__ == "__main__":
    bot.run(token=TOKEN, log_handler=handler, log_level=logging.DEBUG)