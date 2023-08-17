# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import logging
import typing as t

import datetime as dt

from pyhafas import HafasClient
from pyhafas.profile import DBProfile

from rex.model import TravelLocation, TravelPlan
from rex.util.cli import split_list
from rex.util.date import next_date_by_weekday, format_date_weekday

logger = logging.getLogger()


DEFAULT_DEPARTURE_TIME = dt.time(hour=9)
DEFAULT_ARRIVAL_TIME = dt.time(hour=17)
DEFAULT_STOP_DELTA = dt.timedelta(days=1)


def make_travelplan(origin: str, destination: str, stops: t.List[str], when: str):
    client = HafasClient(DBProfile())

    # Resolve home and remote locations.
    location_home = client.locations(origin)[0]
    location_remote = client.locations(destination)[0]

    # Resolve departure and arrival times of home and remote locations.
    on_begin, on_end = split_list(when, delimiter="-")
    date_begin = next_date_by_weekday(on_begin)
    date_end = next_date_by_weekday(on_end, start=date_begin)
    datetime_begin = dt.datetime.combine(date_begin, DEFAULT_DEPARTURE_TIME)
    datetime_end = dt.datetime.combine(date_end, DEFAULT_ARRIVAL_TIME)

    # Report an intermediate summary.
    logger.info(
        f"You will be travelling from {format_date_weekday(datetime_begin)} "
        f"until {format_date_weekday(datetime_end)}"
    )
    logger.info(
        f"You are starting from {origin}, and will visit {destination} "
        f"with stops in {' and '.join(stops)} for {DEFAULT_STOP_DELTA.days} days each"
    )

    # Build a travel plan draft, with home and remote locations, and eventual stops.
    plan = TravelPlan()
    if stops:
        location_start = location_home
        segment_departure = datetime_begin
        for stop in stops:
            location_stop = client.locations(stop)[0]
            segment = TravelLocation(origin=location_start, destination=location_stop, departure=segment_departure)
            plan.append(segment)
            location_start = location_stop
            segment_departure += DEFAULT_STOP_DELTA
        last_segment = TravelLocation(origin=location_start, destination=location_remote, departure=segment_departure)
        plan.append(last_segment)
    else:
        towards = TravelLocation(origin=location_home, destination=location_remote, departure=datetime_begin)
        plan.append(towards)

    back = TravelLocation(origin=location_remote, destination=location_home, arrival=datetime_end)
    plan.append(back)

    logger.info(f"Travel plan draft: Locations\n{plan}")
