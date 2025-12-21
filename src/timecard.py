"""
Datetime logic for Calculating details about payperiods
"""

from datetime import timedelta, date
import holidays
import calendar
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL_AID = os.getenv("EMAIL_AID", "")


def build_payperiod(today:date|None= None) -> list[date]:
    """
    Takes a optional datetime.date object, defalts to today.

    Returns a list of date objects that make up the pay period
    including the provided date.
    """
    today = today or date.today()

    if today.day <=15:
        start = date(today.year, today.month, 1)
        end = date(today.year, today.month, 15)
    else:
        start = date(today.year, today.month, 16)
        month_end = calendar.monthrange(today.year, today.month)[1]
        end = date(today.year, today.month, month_end)

    return [
        start + timedelta(days = i)
        for i in range((end-start).days + 1)
    ]

def calculate_hours(payperiod: list[date]) -> int:
    """
    Returns the number of hours hours required for a payperiod.

    hours = number of week days * 8
    """
    return sum((8 for d in payperiod if d.weekday() < 5))

def count_holidays(payperiod: list[date]) -> list[str]:
    """
    Returns the list of holidays in a given list of dates objects
    """
    years = {d.year for d in payperiod}
    us_holidays = holidays.US(years=years)
    period_holidays = []
    for d in payperiod:
        if d in us_holidays.keys():
            period_holidays.append(us_holidays.get(d))

    return period_holidays

def summarize_payperiod(today=None) -> str:
    """
    Returns a brief summary of the payperiod that the provided date is in.
    """
    period = build_payperiod(today=today)
    period_holidays = count_holidays(period)
    hours = calculate_hours(period)
    holidays_str = " and ".join(period_holidays)
    if period_holidays:
        return f"This payperiod has {hours} hours and {len(period_holidays)} holiday(s): {holidays_str}."
    else:
        return f"This payperiod has {hours} hours with no holidays."
    
def timecard_reminder(): 
    return """
@everyone it's timecard day. {} 
If you are having login issues email the following ASAP: {}
""".format(summarize_payperiod(), EMAIL_AID)

print(timecard_reminder())