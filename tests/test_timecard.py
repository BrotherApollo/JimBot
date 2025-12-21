from src.timecard import build_payperiod, calculate_hours, count_holidays
from datetime import date


def test_build_payperiod():
    # Testing 1st - 15th
    dates = build_payperiod(today=date(2025, 12, 15))
    assert len(dates) == 15

    # Testing 31 day month
    dates = build_payperiod(today=date(2025, 12, 17))
    assert len(dates) == 16

    # Testing 30 day month
    dates = build_payperiod(today=date(2025, 11, 17))
    assert len(dates) == 15

    # Testing Feb
    dates = build_payperiod(today=date(2025, 2, 19))
    assert len(dates) == 13

    # Testing Feb on Leap year
    dates = build_payperiod(today=date(2024, 2, 19))
    assert len(dates) == 14


def test_hours():
    # 96 hours
    dates = build_payperiod(today=date(2025, 12, 17))
    hours = calculate_hours(dates)
    assert hours == 96

    # 88 hours
    dates = build_payperiod(today=date(2025, 12, 14))
    hours = calculate_hours(dates)
    assert hours == 88

    # 80 hours
    dates = build_payperiod(today=date(2025, 11, 17))
    hours = calculate_hours(dates)
    assert hours == 80


def test_holidays():
    dates = build_payperiod(today=date(2025, 12, 17))
    holidays = count_holidays(dates)
    assert len(holidays) == 1

    dates = build_payperiod(today=date(2025, 12, 14))
    holidays = count_holidays(dates)
    assert len(holidays) == 0

    dates = build_payperiod(today=date(2025, 11, 1))
    holidays = count_holidays(dates)
    assert len(holidays) == 1
