# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import datetime as dt
import dataclasses
import io
import json
import typing as t
from enum import Enum

from pyhafas.types.fptf import Station, Journey


@dataclasses.dataclass
class TravelPlanLocation:
    """
    Represent a single travel location.
    """

    origin: Station
    destination: Station
    departure: t.Optional[dt.datetime] = None
    arrival: t.Optional[dt.datetime] = None
    hafas_journeys: t.List[Journey] = dataclasses.field(default_factory=list)
    travel_journeys: t.List["TravelJourney"] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class TravelPlan:
    """
    Represent multiple travel locations.
    """

    locations: t.List[TravelPlanLocation] = dataclasses.field(default_factory=list)

    def append(self, *items: TravelPlanLocation):
        for item in items:
            self.locations.append(item)

    def __str__(self):
        buffer = io.StringIO()
        for location in self.locations:
            data = location.origin.__dict__
            data["when"] = {"departure": str(location.departure), "arrival": str(location.arrival)}
            buffer.write(json.dumps(data, indent=2))
            buffer.write("\n")
        buffer.seek(0)
        return buffer.read()


@dataclasses.dataclass
class TravelJourneySegment:
    """
    Represent a single travel segment.
    """

    time: str
    transport: str
    details: str
    status: t.Optional[str] = None


@dataclasses.dataclass
class TravelJourney:
    """
    Represent a whole travel journey.
    """

    duration: dt.timedelta
    date: dt.date
    segments: t.List[TravelJourneySegment] = dataclasses.field(default_factory=list)

    def append(self, *items: TravelJourneySegment):
        for item in items:
            self.segments.append(item)


class TimeMode(Enum):
    """
    Represent a mode whether to compute journey by departure or arrival time.
    """

    DEPARTURE = "departure"
    ARRIVAL = "arrival"
