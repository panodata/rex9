# remote eXpress


## About

reX9 is a public transport routing software based on time, locations, interests,
and heuristics.


## Details

It obtains rough user constraints like time ranges, an optional travel destination
and further stops on the trip, and computes travel plan drafts using the [HAFAS] API.


## Usage

```shell
rex9 travel --from=Oranienburg --to=Stralsund --stops=Fürstenberg,Mildenberg --on=do-di
```


## Glossary

- Travel: A complete travel plan draft, including multiple journeys.
- Travel segment: A single journey of a travel plan.
- Journey: A HAFAS entity representing a journey, possibly with multiple vehicles.
- Leg or Trip: A HAFAS entity representing a part of a journey with a single vehicle.


## Setup

```shell
git clone https://github.com/panodata/rex9
cd rex9
python3 -m venv .venv
source .venv/bin/activate
pip install --editable=.[develop,docs,test]
```


[HAFAS]: https://de.wikipedia.org/wiki/HAFAS
