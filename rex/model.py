# Copyright (c) 2023, The Panodata developers and contributors.
# Distributed under the terms of the AGPLv3 license, see LICENSE.

import datetime as dt
import dataclasses
import io
import json
import typing as t

from pyhafas.types.fptf import Station


@dataclasses.dataclass
class TravelLocation:
    origin: Station
    destination: Station
    departure: t.Optional[dt.datetime] = None
    arrival: t.Optional[dt.datetime] = None


@dataclasses.dataclass
class TravelPlan:
    locations: t.List[TravelLocation] = dataclasses.field(default_factory=list)

    def append(self, *items: TravelLocation):
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
