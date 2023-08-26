# Routing Engines


## Street Routing

### GraphHopper

GraphHopper is a fast and memory efficient open source routing library and server
written in Java. Designed for the server, desktop, as well as for mobile devices.
It can make use of different algorithms such as Dijkstra, A* and Contraction
Hierarchies.

- https://www.graphhopper.com/
- https://wiki.openstreetmap.org/wiki/GraphHopper
- https://docs.graphhopper.com/#tag/Isochrone-API
- https://docs.graphhopper.com/#section/Map-Data-and-Routing-Profiles
- https://discuss.graphhopper.com/t/getting-distance-between-any-two-points-along-the-train-track-railway/7070
- https://github.com/graphhopper/graphhopper/blob/master/docs/core/profiles.md
- On waterways: https://github.com/graphhopper/graphhopper/commit/8d331af726e6b

### OpenRailRouting

A routing engine for railways based on a forked version of the GraphHopper routing engine
and OpenStreetMap data.

- https://github.com/geofabrik/OpenRailRouting

### Openrouteservice

Openrouteservice is much more than a website with a route service for cars, pedestrians
and bicycles based on Open Standards and Open Geodata. Several Location Based Services
(LBS) created from OSM data are available.

It is developed by HeiGIT - Heidelberg Institute for Geoinformation Technology.

- https://openrouteservice.org/
- https://wiki.openstreetmap.org/wiki/Openrouteservice

### Open Source Routing Machine (OSRM)

High performance routing engine written in C++ designed to run on OpenStreetMap data.

- https://github.com/Project-OSRM/osrm-backend
- https://map.project-osrm.org/

### Valhalla

Valhalla is an open-source routing engine and accompanying set of libraries for use
with OpenStreetMap data. Valhalla is used within Mapzen and Mapbox services and SDKs. 

> Valhalla is a multipurpose routing engine originally created by Mapzen's mobility
> team, which was led by and included the founders of Interline. Now, Valhalla is
> also used by organizations like Mapillary (street imagery), Mapbox (mapping APIs),
> Tesla (electric cars), and Sidewalk Labs (urban real-estate development and
> operations).

- https://www.interline.io/valhalla/
- https://valhalla.github.io/valhalla/
- https://github.com/valhalla/valhalla
- https://wiki.openstreetmap.org/wiki/Valhalla
- https://valhalla.github.io/valhalla/api/isochrone/api-reference/
- https://valhalla.github.io/valhalla/api/turn-by-turn/api-reference/#locations
- https://valhalla.github.io/valhalla/api/turn-by-turn/api-reference/#costing-models
- https://valhalla.github.io/valhalla/api/turn-by-turn/api-reference/#costing-options

Valhalla is open-source (MIT license) and is maintained by many contributors.
Interline continues its involvement in open-source Valhalla, providing a variety
of products and services to help organizations and individuals use Valhalla.


## Multimodel Routing

### OpenTripPlanner (OTP)

Multimodal Trip Planning.

> OpenTripPlanner (OTP) is a family of open source software projects that provide
> passenger information and transportation network analysis services.
>
> The core server-side Java component finds itineraries combining transit, pedestrian,
> bicycle, and car segments through networks built from widely available, open standard
> OpenStreetMap and GTFS data.
>
> This service can be accessed directly via its web API or using a range of Javascript
> client libraries, including modern reactive modular components targeting mobile platforms.

- https://www.opentripplanner.org/
- https://wiki.openstreetmap.org/wiki/OpenTripPlanner
- https://github.com/opentripplanner/OpenTripPlanner
- https://docs.opentripplanner.org/en/dev-2.x/Basic-Tutorial/
- https://docs.opentripplanner.org/en/dev-2.x/Deployments/
- https://github.com/opentripplanner/OpenTripPlanner/blob/dev-2.x/ARCHITECTURE.md
- https://cran.r-project.org/web/packages/opentripplanner/vignettes/opentripplanner.html
- https://docs.ropensci.org/opentripplanner/articles/opentripplanner.html#getting-data-for-otp

### MOTIS

MOTIS is a Multi Objective Travel Information System aka.
Intermodal Mobility Information System, out of TU Darmstadt.

Felix Gündling and Pablo Hoch are the main contributors.

In addition to OSRM and PPR, MOTIS supports the Valhalla street routing engine.
Nigiri is their next generation routing engine. 

- https://motis-project.de/
- https://www.algo.informatik.tu-darmstadt.de/#motis
- https://www.informatik.tu-darmstadt.de/fb20/aktuelles_fb20/fb20_neuigkeiten/neuigkeiten_fb20_details_271168.de.jsp
- https://github.com/motis-project/motis
- https://github.com/motis-project/osrm-backend
- https://github.com/motis-project/ppr
- https://github.com/motis-project/nigiri

> With the new MOTIS v0.11 release, we’re happy to announce that we are almost finished
> with transitioning the intermodal door-to-door real-time routing over to the new
> nigiri core.
>
> -- https://motis-project.de/release/2023/07/14/valhalla.html

- Feature: Intermodal and Timetable Routing from Door to Door
  https://motis-project.de/docs/features/routing.html
- Example: Intermodal Routing Request
  https://motis-project.de/docs/api/endpoint/intermodal.html#intermodal-routing-request
- Web Interface:
  - https://europe.motis-project.de/
  - https://switzerland.motis-project.de/
