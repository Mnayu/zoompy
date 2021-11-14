
Zoompy is a Python wrapper for calling the Ergast API, to get data related to Formula 1. It can be used to get the races, results, driver standings, constructors standings and qualifying results from any year or from a custom duration

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install zoompy.

```bash
pip install zoompy==0.1.3
```

## Usage
#### To obtain any of the data it is neccesary to first obtain the races in that particular time frame and then get the rounds in those season(s).
### Obtaining Lists of Races
```python
zoompy.races(start_year,end_year)

# To obtain races from 2020
zoompy.races(2020,2021)
```
### Obtaining Rounds
```python
races = zoompy.races(2020,2021)

rounds = zoompy.get_rounds(races)

```
### Obtaining Results
```python
races = zoompy.races(2020,2021)

rounds = zoompy.get_rounds(races)

results= zoompy.results(rounds)

```
### Obtaining Driver Standing
```python
races = zoompy.races(2020,2021)

rounds = zoompy.get_rounds(races)

d_standings= zoompy.driver_Standings(rounds)

```
### Obtaining Constructor Standing
```python
races = zoompy.races(2020,2021)

rounds = zoompy.get_rounds(races)

c_standings= zoompy.constructor_standings(rounds)

```
### Obtaining Qualifying data
```python
zoompy.qualifying(start_year,end_year)

#obtaining qualifying results from 2020
qualifying= zoompy.qualifying(2020,2021)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
