# network-outage-duration-calculator

Turn an outage log into durations per outage, longest first, with ongoing outages reported separately and excluded from the completed total.

## How to run

```sh
python3 main.py outages.csv
```

## Example output

```
OUT-2: 60 minutes
OUT-1: 30 minutes
Total completed outage time: 90 minutes; 0 ongoing.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
