# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import datetime as dt

from aika import DaterangeExpression
from freezegun import freeze_time

TESTDRIVE_DATETIME = "2023-08-17T23:03:17+0200"


@freeze_time(TESTDRIVE_DATETIME)
def test_parse_daterange_relative_months():
    dr = DaterangeExpression(
        default_start_time=dt.time(hour=9),
        default_end_time=dt.time(hour=17),
    )
    assert (
        dr.parse("next March")
        == dr.parse("im März")
        == (
            dt.datetime(2023, 3, 1, 9, 0, 0),
            dt.datetime(2023, 3, 31, 17, 0, 0),
        )
    )
    assert (
        dr.parse("July to December")
        == dr.parse("Juli bis Dezember")
        == (
            dt.datetime(2023, 7, 1, 9, 0, 0),
            dt.datetime(2023, 12, 31, 17, 0, 0),
        )
    )


@freeze_time(TESTDRIVE_DATETIME)
def test_parse_daterange_relative_weekdays():
    dr = DaterangeExpression(
        default_start_time=dt.time(hour=9),
        default_end_time=dt.time(hour=17),
    )
    assert (
        dr.parse("Sat - Tue")
        == dr.parse("Sa-Di")
        == (
            dt.datetime(2023, 8, 19, 9, 0, 0),
            dt.datetime(2023, 8, 22, 17, 0, 0),
        )
    )
