# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import datetime as dt
import typing as t


def format_date_weekday(datetime: dt.datetime):
    return f"{datetime} ({datetime.strftime('%A')})"


def format_time(value: t.Union[dt.datetime, dt.time]) -> str:
    return value.strftime("%H:%M")
