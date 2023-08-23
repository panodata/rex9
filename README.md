# remote eXpress


## About

reX9 is a public transport routing software based on time, locations, interests,
and heuristics, with a strong aim for providing a [DWIM]-like interface.


## Details

It obtains rough user constraints like time ranges, an optional travel destination
and further stops on the trip, and computes travel plan drafts using the [HAFAS] API.


## Setup

Install the most recent version of reX9.
```shell
pip install --upgrade 'git+https://github.com/panodata/rex9'
```


## Usage

```shell
rex9 travel --from=Oranienburg --to=Stralsund --stops=Fürstenberg,Mildenberg --when=do-di
```

The `--when` argument accepts all date-/time-range expressions as provided by the [Aika]
package, which currently supports English and German.


## Glossary

- Travel: A complete travel plan draft, including multiple journeys.
- Travel segment: A single journey of a travel plan.
- Journey: A HAFAS entity representing a journey, possibly with multiple vehicles.
- Leg or Trip: A HAFAS entity representing a part of a journey with a single vehicle.


## Development

Acquire source code and install development sandbox.
```shell
git clone https://github.com/panodata/rex9
cd rex9
python3 -m venv .venv
source .venv/bin/activate
pip install --editable='.[develop,docs,test]'
```

Run linters and software tests:
```shell
source .venv/bin/activate
poe check
```


[Aika]: https://github.com/panodata/aika
[DWIM]: https://en.wikipedia.org/wiki/DWIM
[HAFAS]: https://de.wikipedia.org/wiki/HAFAS
