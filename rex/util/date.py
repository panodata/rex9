# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import datetime as dt
import dateutil.relativedelta as dtrel


class WeekdayMap:
    days_en = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    days_de = ["MO", "DI", "MI", "DO", "FR", "SA", "SO"]

    def __init__(self):
        self.weekdays = {}
        for index, day in enumerate(self.days_en):
            self.weekdays[day] = dtrel.weekday(index)
        for index, day in enumerate(self.days_de):
            self.weekdays[day] = dtrel.weekday(index)

    def find(self, label: str):
        for key, value in self.weekdays.items():
            if key.lower().startswith(label.lower()):
                return value
        raise KeyError(f"Weekday not found: {label}")


def next_date_by_weekday(weekday: str, start=dt.date.today()):
    weekday_map = WeekdayMap()
    weekday_dtrel = weekday_map.find(weekday)
    delta = dtrel.relativedelta(days=1, weekday=weekday_dtrel)
    next_friday = start + delta
    return next_friday


def format_date_weekday(datetime: dt.datetime):
    return f"{datetime} ({datetime.strftime('%A')})"
