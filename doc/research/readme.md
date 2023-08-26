# reX9 Research


## About

Let's scan the FOSS and Open Data ecosystems for building blocks to conceive reX9.
This is a non-exhaustive collection of information, and contributions are always
welcome.


## Introduction

There are both publicly accessible open data APIs and FOSS software projects
already, to easily conduct some first experiments, and to dive deeper into the
topics of multimodal and intermodal routing.

Specifically, to check whether and how they can be useful for reX9, we should
evaluate a few of the most interesting and capable FOSS routing engines, before
attempting to reinvent the wheel.


## Details

### Street routing vs. public transport routing

In general, one has to discriminate between street routing and public transport routing.
In FOSS and Open Data lands, street routing is usually based on OSM data, while public
transport routing is usually based on GTFS data.

There are exceptions, like open data provided on a national or regional level through
systems like HAFAS, mostly in Germany and Europe, or hybrid routing modes, for example
doing street-based routing on railway tracks.

### Intermodal routing

A combination of both, or more, to support arbitrary transport modes such as public
transport, walking, driving by car (own car, taxi, etc.), ride sharing, bike sharing,
or flights, is called "intermodal routing", "multimodal trip planning", or
"multi-modal transportation".

### Travel time maps / Isochrones

Measuring distance by accessibility time is sensible to evaluate which destinations
can be reached in a certain amount of time.

> An isochrone is an isoline for travel time, that is a curve of equal travel time.
> Closely related is isodistance, which is a curve of equal travel distance.
>
> -- https://wiki.openstreetmap.org/wiki/Isochrone


## Resources

- [APIs](api.md)
- [Deutsche Bahn](deutsche-bahn.md)
- [HAFAS](hafas.md)
- [Mobile Network Coverage](mobile-network-coverage.md)
- [Organizations](organization.md)
- [Scientific Resources and Papers](scientific.md)
- [Software: Components](software-component.md)
- [Software: Routing Engines](software-routing-engine.md)
- [Software: Travel Planning](software-travel-planner.md)
- [Standards and Specifications](standard-and-spec.md)
- [Travel Time Maps](travel-time-maps.md)
- [Unsorted](unsorted.md)
