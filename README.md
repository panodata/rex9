# remote eXpress


## About

reX is a public transport routing software based on time, locations, interests,
and heuristics.


## Details

It obtains rough user constraints like time ranges, an optional travel destination
and further stops on the trip, and computes travel plan drafts using the [HAFAS] API.


## Setup

```shell
git clone https://github.com/panodata/rex
cd rex
python3 -m venv .venv
source .venv/bin/activate
pip install --editable=.[develop,docs,test]
```


## Usage

```shell
rex travel --from=Oranienburg --to=Kopenhagen --stops=Fürstenberg,Mildenberg --on=do-di
```


[HAFAS]: https://de.wikipedia.org/wiki/HAFAS
