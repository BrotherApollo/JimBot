from datetime import timedelta, date
import holidays
import calendar


def build_payperiod(today=None):
    if today == None:
        today = date.today()
    
    if today.day <=15:
        start = date(today.year, today.month, 1)
        end = date(today.year, today.month, 15)
    else:
        start = date(today.year, today.month, 16)
        monthEnd = calendar.monthrange(today.year, today.month)[1]
        end = date(today.year, today.month, monthEnd)

    return [
        start + timedelta(days = i)
        for i in range((end-start).days + 1)
    ]

def calculate_hours(payperiod: list[date]):
    hours = 0
    for d in payperiod:
        if d.weekday() < 5:
            hours += 8
    
    return hours

def count_holidays(payperiod: list[date]) -> list[str]:
    today = payperiod[0]
    us_holidays = holidays.US(years=today.year)
    period_holidays = []
    for d in payperiod:
        if d in us_holidays.keys():
            period_holidays.append(us_holidays.get(d))

    return period_holidays

def summarize_payperiod(today=None):
    period = build_payperiod(today=today)
    holidays = count_holidays(period)
    hours = calculate_hours(period)
    holidays_str = " and ".join(holidays)
    return f"This is an {hours} payperiod with {len(holidays)} holiday(s): {holidays_str}"

# print(len(build_payperiod()))
# print(calculate_hours(build_payperiod()))

r = build_payperiod()
print(count_holidays(r))