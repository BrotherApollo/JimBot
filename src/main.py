import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# Local Imports
from timecard import summarize_payperiod

# Loading discord token form environement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TIMECARD_CHANNEL = 1323403232822689805

# Scheduler
scheduler = AsyncIOScheduler()

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
    """Responds to !timecard messages in the same channel"""
    await ctx.send(summarize_payperiod())

# Scheduled Reminders
async def send_timecard_reminder():
    """Post timecard reminders in a specific channel"""
    channel = bot.get_channel(TIMECARD_CHANNEL)
    await channel.send(summarize_payperiod())

@bot.event
async def on_ready():
    """Initilization, includes all schduled jobs"""
    if scheduler.running:
        return

    print(f"Logged in as {bot.user}")

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
    
    # # Test
    # scheduler.add_job(
    #     lambda: bot.loop.create_task(send_timecard_reminder()),
    #     CronTrigger(day=18, hour=18, minute=30)
    #     )
    
    scheduler.start()    

bot.run(token=TOKEN, log_handler=handler, log_level=logging.DEBUG)