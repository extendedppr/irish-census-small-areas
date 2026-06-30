# Irish Census Small Area Data

Scrape Irish census small area data for friendly programmatic usage. The country is broken into roughly 19,000 areas giving pretty good granularity. Interactive map [here](https://visual.cso.ie/?body=entity/ima/cop/2022)

Not fully complete as I only need a fraction for the projects I'm concerned with, mainly to do with mapping and properties of areas but I'll add others over time.

Also only using for 2022 for the moment.


## Installation

```bash
poetry install
```


## Scraping data

```bash
# To download all, takes a long time
poetry run download
# To download single
poetry run download --type occupations
```


## Usage

When specifying a radius around a point this will use all small areas whose centers are within the radius, not all areas that are within the radius.

```bash
poetry run get_stats_around_area --lat 53.5 --lng -6.5 --radius-km 5
```


## Test

```bash
poetry install --with test
poetry run pytest
```
