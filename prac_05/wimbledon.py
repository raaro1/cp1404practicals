"""
wimbledon
Estimate: 50 minutes
Actual:   60 minutes
"""


FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and display details about Wimbledon champions and countries."""
    match_records = load_records(FILENAME)
    champion_to_count, countries = process_records(match_records)
    show_results(champion_to_count, countries)


def load_records(filename):
    """Read CSV file and return list of lists containing record data."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Skip the header row
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champions and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def show_results(champion_to_count, countries):
    """Display champions and list of winning countries."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_count.items()):
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))



main()

