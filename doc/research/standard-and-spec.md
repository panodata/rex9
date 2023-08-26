# Standards

Enumerating open data standards, hubs, and specifications, for public transport and beyond.

## Deutsche Bahn Datasets

- https://data.deutschebahn.com/dataset.groups.datasets.html

## Friendly Public Transport Format (FPTF)

Conceptually inspired by the de-facto standard GTFS, but aligned with HAFAS.

- https://github.com/public-transport/friendly-public-transport-format
- https://github.com/public-transport/friendly-public-transport-format/blob/master/modules.md


## GTFS

### About

The General Transit Feed Specification (GTFS) is an Open Standard used to
distribute relevant information about transit systems to riders.

### Details

It allows public transit agencies to publish their transit data in a format that
can be consumed by a wide variety of software applications. Today, the GTFS data
format is used by thousands of public transport providers.

GTFS consists of two main parts: GTFS Schedule and GTFS Realtime. GTFS Schedule
contains information about routes, schedules, fares, and geographic transit
details, and it is presented in simple text files. This straightforward format
allows for easy creation and maintenance without relying on complex or
proprietary software.

GTFS Realtime contains trip updates, vehicle positions, and service alerts. It
is based on Protocol Buffers, which are a language (and platform) neutral
mechanism for serializing structured data.

### Resources 

- https://gtfs.org/
- https://developers.google.com/transit/gtfs/
- https://developers.google.com/transit/gtfs-realtime
- https://developers.google.com/transit/gtfs-realtime/examples/python-sample
- https://www.transit.land/
- awesome-transit
  Community list of transit APIs, apps, datasets, research, and software 🚌🌟🚋🌟🚂
  https://github.com/CUTR-at-USF/awesome-transit

### The Mobility Database

The Mobility Database Catalogs is a list of open mobility data sources from
across the world.

- https://database.mobilitydata.org/
- https://github.com/MobilityData
- https://github.com/MobilityData/mobility-database-catalogs
- https://github.com/MobilityData/gbfs

> If you are only interested in browsing the sources or pulling all the latest URLs,
> [download the CSV](https://bit.ly/catalogs-csv). You can cross-reference IDs from
> the Mobility Database, TransitFeeds and Transitland with [this ID map spreadsheet](https://docs.google.com/spreadsheets/d/1Q96KDppKsn2khdrkraZCQ7T_qRSfwj7WsvqXvuMt4Bc/edit?resourcekey#gid=1787149399).

- https://github.com/MobilityData/gtfs-flex

### More Resources

- VBB-Fahrplandaten via GTFS
  https://daten.berlin.de/datensaetze/vbb-fahrplandaten-gtfs
- https://www.vbb.de/vbbgtfs
- https://storage.googleapis.com/storage/v1/b/mdb-latest/o/de-berlin-verkehrsverbund-berlin-brandenburg-gtfs-782.zip?alt=media


## IBNR

Die Interne Bahnhofsnummer (IBNR) ist ein Indikator bei der Deutschen Bahn zur tariflichen
Identifikation von Personenbahnhöfen in Deutschland und anderen europäischen Ländern. Die
IBNR umfasst in der Regel fünf Stellen, mit UIC-Ländercode sieben Stellen. 

- https://de.wikipedia.org/wiki/Internationale_Bahnhofsnummer
- https://www.michaeldittrich.de/ibnr/
- https://data.deutschebahn.com/dataset/data-haltestellen.html
- https://wiki.openstreetmap.org/w/images/c/c2/20141001_IBNR.pdf
