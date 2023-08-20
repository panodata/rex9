# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import logging
import typing as t

import datetime as dt
from textwrap import indent

from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Remark

from rex9.model import TravelPlanSegment, TravelPlan, TravelJourney, TravelJourneySegment, TimeMode
from rex9.util.cli import split_list
from rex9.util.date import next_date_by_weekday, format_date_weekday, format_time
from rex9.util.pyhafas import query_for

logger = logging.getLogger()


# TODO: Make configurable.
DEFAULT_DEPARTURE_TIME = dt.time(hour=9)
DEFAULT_ARRIVAL_TIME = dt.time(hour=17)
DEFAULT_STOP_DELTA = dt.timedelta(days=1)
DEFAULT_MAX_CHANGES = -1
DEFAULT_MIN_CHANGE_TIME = 3

# Suppress "Fahrzeuggebundene Einstiegshilfe vorhanden"
DEFAULT_REMARKS_FILTER = ["A/EH"]


def make_travelplan(origin: str, destination: str, stops: t.List[str], when: str):
    """
    Obtain travel parameters and compute a travel plan draft.
    """
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

    # Build a travel plan draft, with home and remote locations, and optional stops.
    plan = TravelPlan()
    if stops:
        location_start = location_home
        segment_departure = datetime_begin
        for stop in stops:
            location_stop = client.locations(stop)[0]
            segment = TravelPlanSegment(origin=location_start, destination=location_stop, departure=segment_departure)
            plan.append(segment)
            location_start = location_stop
            segment_departure += DEFAULT_STOP_DELTA
        last_segment = TravelPlanSegment(
            origin=location_start, destination=location_remote, departure=segment_departure
        )
        plan.append(last_segment)
    else:
        trip_outbound = TravelPlanSegment(origin=location_home, destination=location_remote, departure=datetime_begin)
        plan.append(trip_outbound)

    trip_return = TravelPlanSegment(origin=location_remote, destination=location_home, arrival=datetime_end)
    plan.append(trip_return)

    logger.debug(f"Travel plan draft: Segments\n{plan}")

    return plan


def compute_journey(plan: TravelPlan):
    """
    Resolve travel plan draft using HAFAS journey information.
    """
    client = HafasClient(DBProfile())
    for segment in plan.segments:
        if segment.departure and segment.arrival:
            raise ValueError("departure and arrival are mutually exclusive")

        # Either query by departure time (default), or by arrival time.
        mode = TimeMode.DEPARTURE
        when = segment.departure
        if segment.arrival:
            mode = TimeMode.ARRIVAL
            when = segment.arrival
        with query_for(client, mode):
            segment.hafas_journeys = client.journeys(
                origin=segment.origin,
                destination=segment.destination,
                date=when,
                max_changes=DEFAULT_MAX_CHANGES,
                min_change_time=DEFAULT_MIN_CHANGE_TIME,
            )

        # Iterate HAFAS journey recommendations.
        # - In:  HAFAS journeys and legs/trips.
        # - Out: TravelJourney and TravelJourneySegment entities.
        for journey in segment.hafas_journeys:
            travel_journey = TravelJourney(duration=journey.duration, date=journey.date)
            for leg in journey.legs:
                label = str(leg.mode.value)
                if leg.name:
                    label += f" {leg.name}"

                platforms = ""
                if leg.departurePlatform is not None and leg.arrivalPlatform is not None:
                    platforms = f"Platforms {leg.departurePlatform}/{leg.arrivalPlatform} "
                details = f"{platforms}from {leg.origin.name} to {leg.destination.name}"

                item = TravelJourneySegment(
                    time=f"{format_time(leg.departure.time())}-{format_time(leg.arrival.time())}",
                    transport=label,
                    details=details,
                    remarks=bulletpoints(format_remarks(leg.remarks), level=2),
                )
                if leg.departureDelay is not None or leg.arrivalDelay is not None:
                    item.status = f"Delays: {leg.departureDelay} {leg.arrivalDelay}"
                travel_journey.append(item)

            segment.travel_journeys.append(travel_journey)


def format_remarks(remarks: t.List[Remark]) -> t.List[str]:
    """
    Format information from a list of FPTF Remark objects.
    """
    parts = []
    for remark in remarks:
        code = f"{remark.remark_type}/{remark.code}"
        if code in DEFAULT_REMARKS_FILTER:
            continue
        text = remark.text
        if remark.subject is not None:
            text = f"{remark.subject} {text}"
        part = f"{code}: {text}"
        parts.append(part)
    return parts


def bulletpoints(items: t.List[str], level: int = 0):
    """
    Format list items as bullet points.
    """
    prefix = " " * (level * 2)
    return indent("\n".join(items), prefix=f"{prefix}- ")
