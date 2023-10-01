# Standards

Enumerating open data standards, hubs, and specifications, for public transport and beyond.

[MOTIS](#motis) already uses OSM, GTFS or HRD, and OSRM_PROFILE,
see https://github.com/motis-project/motis/issues/13.


## DELFI

DELFI, die Durchgängige ELektronische FahrgastInformation, setzt sowohl den technologischen
als auch den organisatorischen Rahmen für eine einheitliche Routenberechnung im öffentlichen
Personenverkehr in Deutschland. Die DELFI-Produkte, insbesondere der deutschlandweite DELFI-
Datensatz sowie das Zentrale Haltestellenverzeichnis bilden die Grundlage für zukunftsfähige
Informationsdienste von Morgen - zuverlässig, transparent, hochaktuell.

DELFI ist ein Kooperationsnetzwerk aller Bundesländer, des Bundes sowie weiterer Partner und
schafft die technischen Voraussetzungen zur Beauskunftung bundeslandübergreifender Reiseketten.
Der DELFI e.V. agiert als organisatorische Schaltstelle zwischen den Interessen der
Kooperationspartner und treibt technologische und fachliche Innovationen in den Bereichen
Harmonisierung, Durchgängigkeit und Interoperabilität von Serviceangeboten im Verkehr voran.

In der Regel werden die aktuellen GTFS-, NeTEx und zHV Daten montags bereitgestellt. Fällt der
Montag auf einen gesetzlichen Feiertag in Hessen ist eine Bereitstellung am nächsten Werktag
(Mo-Fr) geplant.

- https://www.delfi.de/
- https://www.delfi.de/de/leistungen-produkte/daten-dienste/
- https://www.opendata-oepnv.de/ht/de/organisation/delfi/startseite
- https://invidious.fdn.fr/watch?v=H8OX2N3uKCk
- https://www.opendata-oepnv.de/ht/de/news-trends/detailanzeige?tx_news_pi1[action]=detail&tx_news_pi1[controller]=News&tx_news_pi1[news]=255
- https://www.zukunftsplattform-nahverkehr.de/public/events/be05b1abbd/companies/ef641321f5

### DELFI-Datensatz

Die Fahrplansolldaten aus den Landesauskunftssystemen werden in der DELFI-Integrationsplattform
(DIP) zu einem Datenpool zusammengeführt. Durch einen Datenexport aus der DIP entsteht auf dieser
Basis der deutschlandweite, routingfähige DELFI-Datensatz, der in unterschiedlichen Formaten als
Produkt bereitgestellt werden kann. Der DELFI-Datensatz vereint das Beste aus zwei Welten:

Er kann zusätzlich zu globalen Suchoptionen auch die eigenen Optionen jedes Landessystems
enthalten. Dies ermöglicht den Einsatz des DELFI-Datensatzes für die Suche im Landessystem
mit den gewohnten regionalen als auch länderübergreifend mit den globalen DELFI-Suchoptionen.
Und schafft so die nötigen Rahmenbedingungen, um optimal und standardisiert zu informieren.

Der DELFI-Datensatz

- ist der veredelte Datenbestand sämtlicher, nationaler Fahrplan-Solldaten als deutschlandweit routingfähiger Datenexport aus der DIP, 
- enthält den ÖPNV der Landessysteme, Schienen-Fernverkehr und Fernbusse  
- ist tagesaktuell, und qualitätsgesichert,
- beinhaltet DHIDs (eindeutige Haltestellen-IDs),
- ermöglicht die direkte Nutzung der Datenbankinhalte der DIP.  

### DELFI-Infodienst

Der DELFI-Infodienst ist ein deutschlandweiter ÖPV-Auskunftsdienst auf Basis des DELFI-
Datensatzes. Der Zugang erfolgt über die TRIAS-Schnittstelle eines DELFI-Landesauskunftssystems
und stellt eine indirekte Nutzung der Datenbankinhalte der DIP dar. Der DELFI-Infodienst bietet
über einen Anreicherungsmechanismus neben dem Routing auf Sollfahrplanbasis auch die 
nachrichtliche Anzeige Zusatzinformationen wie zum Beispiel Prognose- und Störungsinformationen,
sofern diese in den jeweiligen DELFI-Landesauskunftssystemen vorliegen. 

Der DELFI-Infodienst

- erfolgt deutschlandweit,
- ist adressscharf,
- basiert auf dem DELFI-Datensatz,
- beinhaltet markterprobte Router/Routingalgorithmen,
- und erfolgt zusätzlich mit Anreicherung. 

### ZHV-Datensatz

Die Daten aus dem Zentralen Haltestellenverzeichnis (ZHV) stehen allen interessierten Nutzern
kostenlos per Download zur Verfügung. Sie dürfen für die Fahrgastinformation sowohl im Druck
als auch elektronisch genutzt, angezeigt und weiterverarbeitet werden. Gemeinsam mit den
Datenlieferanten aus den unterschiedlichen Regionen und Ländern sorgen wir dafür, dass die
ZHV-Daten in hoher Qualität und aktuell vorliegen. Zudem sind wir für die Verwendung der
DHIDs im DELFI-Datensatz verantwortlich. 

### WMS (Web Mapping Service) - Haltestellenlayer

Der WMS-Haltestellenlayer enthält alle Objekte des ZHV als Geoobjekte (Punktobjekte) mit
referenzierten Attributdaten. Er kann mit anderen Layern kombiniert in Systemen mit
GIS-Komponenten genutzt werden. Er ermöglicht es den Nutzern die Haltestellenobjekte in
Kombination mit anderen Informationsschichten zu visualisieren.


## Deutsche Bahn Datasets

- https://data.deutschebahn.com/dataset.groups.datasets.html


## DINO

DINO steht für Diva-Infopool Nord und ist eine einheitliche Austauschschnittstelle
für Fahrplandaten.

- https://www.connect-fahrplanauskunft.de/index.php?id=21
- https://archiv.opendata-oepnv.de/VRR/Soll-Fahrplandaten/DINO/v2.1/Beschreibung_Austauschformat_DINO_V2.1.2_22.01.2021.pdf


## Friendly Public Transport Format (FPTF)

Conceptually inspired by the de-facto standard GTFS, but aligned with HAFAS.

- https://github.com/public-transport/friendly-public-transport-format
- https://github.com/public-transport/friendly-public-transport-format/blob/master/modules.md


## GTFS

### About

The General Transit Feed Specification (GTFS) is an Open Standard used to
distribute relevant information about transit systems to riders.

It defines a common format for public transportation schedules and associated
geographic information.

### Details

It allows public transit agencies to publish their transit data in a format that
can be consumed by a wide variety of software applications. Today, the GTFS data
format is used by thousands of public transport providers.

GTFS consists of two main parts: GTFS Schedule (or Static) and GTFS Realtime.
GTFS Schedule contains information about routes, schedules, fares, and geographic
transit details, and it is presented in simple text files. This straightforward
format allows for easy creation and maintenance without relying on complex or
proprietary software.

GTFS Realtime contains trip updates, vehicle positions, and service alerts. It
is based on Protocol Buffers, which are a language (and platform) neutral
mechanism for serializing structured data.

- https://en.wikipedia.org/wiki/GTFS
- https://en.wikipedia.org/wiki/GTFS_Realtime

### Resources 

- https://gtfs.org/
- https://developers.google.com/transit/gtfs/
- https://developers.google.com/transit/gtfs-realtime
- https://developers.google.com/transit/gtfs-realtime/examples/python-sample
- https://www.transit.land/
- awesome-transit
  Community list of transit APIs, apps, datasets, research, and software 🚌🌟🚋🌟🚂
  https://github.com/CUTR-at-USF/awesome-transit
- Specification to manipulate General Transit Feed Specification (GTFS) and GTFS Realtime.
  https://github.com/google/transit
- https://github.com/mfdz/GTFS-Issues
- https://projekte.kvv-efa.de/GTFS/google_transit.zip
  - via: https://github.com/opentripplanner/OpenTripPlanner/issues/2780


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


## HAFAS

### About

By Hacon.

- HAFAS.webapp: https://www.hacon.de/fileadmin/user_upload/Portfolio/Factsheets/HAFAS/HAFAS.webapp_english.pdf
- https://www.yumpu.com/en/document/view/13303076/hafas-timetable-information-system-hacon

### HAFAS Raw Data Format (HRDF)

- https://opentransportdata.swiss/en/cookbook/hafas-rohdaten-format-hrdf/
- [HAFAS Raw data file format](https://transportdatamanagement.ch/content/uploads/2020/04/HRDF.5.20.39-Guidelines-e.pdf)
- https://www.öv-info.ch/de/branchenstandard/branchenstandard-kundeninformation-bs-ki/technische-standards

### Resources

- https://github.com/FahrplanDatenGarten/pyhafas
- https://github.com/public-transport/hafas-rest-api
- https://gist.github.com/derhuerst/2b7ed83bfa5f115125a5
- https://sourceforge.net/software/product/HAFAS/


## IBNR

Die Interne Bahnhofsnummer (IBNR) ist ein Indikator bei der Deutschen Bahn zur tariflichen
Identifikation von Personenbahnhöfen in Deutschland und anderen europäischen Ländern. Die
IBNR umfasst in der Regel fünf Stellen, mit UIC-Ländercode sieben Stellen. 

- https://de.wikipedia.org/wiki/Internationale_Bahnhofsnummer
- https://www.michaeldittrich.de/ibnr/
- https://data.deutschebahn.com/dataset/data-haltestellen.html
- https://wiki.openstreetmap.org/w/images/c/c2/20141001_IBNR.pdf


## IFOPT

IFOPT (Identification of Fixed Objects in Public Transport) is a [CEN] Technical
Specification that provides a Reference Data Model for describing the main fixed objects
required for public access to Public transport, that is to say Transportation hubs (such
as airports, stations, bus stops, ports, and other destination places and points of
interest, as well as their entrances, platforms, concourses, internal spaces, equipment,
facilities, accessibility etc.).

- https://en.wikipedia.org/wiki/Identification_of_Fixed_Objects_In_Public_Transport
- https://www.transmodel-cen.eu/ifopt-standard/


## NaPTAN

The National Public Transport Access Node (NaPTAN) database is a UK nationwide system
for uniquely identifying all the points of access to public transport in the UK. The
dataset is closely associated with the National Public Transport Gazetteer. 

- https://en.wikipedia.org/wiki/NaPTAN
- https://wiki.openstreetmap.org/wiki/NaPTAN
- https://www.gov.uk/government/publications/national-public-transport-access-node-schema


## NeTEx

Public transport Network Timetable Exchange (NeTEx) is a technical standard for
exchanging Public Transport Information as XML documents.

The functional scope of NeTEx is divided into three parts, each covering a functional
subset of the CEN Transmodel conceptual model for Public Transport Information, [T1],
[T2], and [T3].
- Part 1 describes the fixed Network (stops, routes, lines, etc.)
- Part 2 [N2] is mainly focused on Timetables and
- Part 3 [N3] covers Fare data (and is the main subject of this paper).

All three parts use the same framework of reusable components, versioning mechanism,
validity conditions, support to allow the uniquely identification of data elements in
a global context, etc., defined in Part 1. NeTEx also includes container elements
called “VERSION FRAMES” to group data into coherent sets for efficient exchange.

Data in NeTEx schema can be used to exchange:

- Public Transport schedules including stops, routes, departures times / frequencies, operational notes, and map coordinates.
- Routes with complex topologies such as circular routes, cloverleaf and lollipops, and complex workings such as short working and express patterns. Connections with other services can also be described
- The days on which the services run, including availability on public holidays and other exceptions.
- Composite journeys such as train journeys that merge or split trains
- Information about the Operators providing the service.
- Additional operational information, including, positioning runs, garages, layovers, duty crews, useful for AVL and on-board ticketing systems.
- Data about the Accessibility of services to passengers with restricted mobility.
- Data is versioned with management metadata allowing updates across distributed systems
- Fare structures, (flat fares, point to point fares, zonal fares)
- Fare products (Single tickets, return tickets, day, and season passses etc)
- Fare prices that apply at specific dates

### Resources

- https://en.wikipedia.org/wiki/NeTEx
- https://netex-cen.eu/
- https://netex-cen.eu/overview/
- https://github.com/NeTEx-CEN/NeTEx
- https://www.vdv.de/netex.aspx
- https://cms.opendata-oepnv.de/fileadmin/Dokumentationen_etc/DELFI/prCEN_TS_16614-PI_Profile_FV__E_-2019_-_Final_Draft.pdf
- https://www.netex-cen.eu/wp-content/uploads/2021/03/NeTEx-extension-for-New-Modes-Detailed-Scope-v04.pdf


## OpenData ÖPNV

Auf diesem Portal veröffentlicht die Initiative „OpenData ÖPNV“ einen wachsenden Datenbestand
rund um Mobilität und alles was dazugehört. Mit dem Portal stellt Ihnen eine Vielzahl von
Tarif- und Verkehrsverbünden Daten zum ÖPNV im jeweiligen Verbundraum zur Verfügung. Die
Initiative orientiert sich an der VDV-Mitteilung 7030, in der OpenData und OpenService
behandelt werden. DELFI stellt deutschlandweite Fahrplandaten gemäß der
Delegierten Verordnung 2017/1926 zur Verfügung.

Enthält [DELFI](#delfi) Datensätze in [GTFS](#gtfs) und [NeTEx](#netex) Formaten. 

- https://www.opendata-oepnv.de/
- https://www.opendata-oepnv.de/ht/de/datensaetze
- https://www.opendata-oepnv.de/ht/de/api
- https://www.opendata-oepnv.de/ht/de/showcases


## OpRa

OpRa is a [CEN] initiative with main focus on the identification of Public Transport
raw data to be exchanged, gathered and stored in order to support Study and Control
of Public Transport Service.

https://www.opra-cen.eu/


## SIRI

Service Interface for Real Time Information (SIRI) is an XML protocol to allow
distributed computers to exchange real-time information about public transport
services and vehicles.

The protocol is a [CEN] norm, developed originally as a technical standard with
initial participation by France, Germany (Verband Deutscher Verkehrsunternehmen),
Scandinavia, and the UK (RTIG). 

- https://en.wikipedia.org/wiki/Service_Interface_for_Real_Time_Information
- https://www.siri-cen.eu/
- https://github.com/SIRI-CEN/SIRI


## TPEG

The Transport Protocol Experts Group (TPEG) is a data protocol suite for traffic and
travel related information. TPEG can be carried over different transmission media
(bearers), such as digital broadcast or cellular networks (wireless Internet). TPEG
applications include, among others, information on road conditions, weather, fuel
prices, parking or delays of public transport. 

- https://en.wikipedia.org/wiki/TPEG
- https://tisa.org/
- https://www.wecantpeg.com/


## Transmodel

Transmodel is the [CEN] European Reference Data Model for Public Transport Information;
it provides a conceptual model of common public transport concepts and data structures
that can be used to build many different kinds of public transport information system,
including for timetabling, fares, operational management, real time data, journey
planning etc. 

- https://en.wikipedia.org/wiki/Transmodel
- https://transmodel-cen.eu/


## TransXChange

TransXChange is a UK national XML based data standard for the interchange of bus
route and timetable information between bus operators, the Vehicle and Operator
Services Agency, local authorities and passenger transport executives, and others
involved in the provision of passenger information. 

- https://en.wikipedia.org/wiki/TransXChange
- https://www.gov.uk/government/collections/transxchange



[CEN]: https://en.wikipedia.org/wiki/European_Committee_for_Standardization


