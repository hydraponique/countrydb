import csv
import gzip
from collections import defaultdict
from pathlib import Path

INPUT_FILE = "ipinfo_lite.csv.gz"

OUTPUT_DIR = Path("geo/geoip")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

countries = defaultdict(list)

with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        country_code = row.get("country_code", "").strip()
        network = row.get("network", "").strip()
        if country_code and network:
            countries[country_code].append(network)

for code, networks in countries.items():
    output_file = OUTPUT_DIR / f"{code.lower()}.lst"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(networks))
