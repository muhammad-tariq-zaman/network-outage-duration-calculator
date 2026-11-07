"""Total outage minutes from an outage log.

Usage: python3 main.py outages.csv
CSV columns: outage_id,start,end (ISO datetimes; end may be empty).
Completed outages get a duration in minutes; empty-end rows are
reported ONGOING and excluded from the total. Longest first.
"""
import argparse, csv, sys
from datetime import datetime

def calculate(rows):
    out, ongoing = [], []
    for row in rows:
        start = datetime.fromisoformat(row["start"].strip())
        end_raw = row["end"].strip()
        if not end_raw:
            ongoing.append(row["outage_id"])
        else:
            minutes = int((datetime.fromisoformat(end_raw) - start).total_seconds() // 60)
            out.append((row["outage_id"], minutes))
    return sorted(out, key=lambda r: -r[1]), ongoing

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        result, ongoing = calculate(list(csv.DictReader(f)))
    total = 0
    for outage, minutes in result:
        total += minutes
        print(f"{outage}: {minutes} minutes")
    for outage in ongoing:
        print(f"{outage}: ONGOING")
    print(f"Total completed outage time: {total} minutes; {len(ongoing)} ongoing.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
