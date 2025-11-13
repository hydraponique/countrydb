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
            if "/" not in network:
                network += "/32"
            countries[country_code].append(network)

for code, networks in countries.items():
    lst_file = OUTPUT_DIR / f"{code.lower()}.lst"
    with open(lst_file, "w", encoding="utf-8") as f:
        f.write("\n".join(networks))

    yaml_file = OUTPUT_DIR / f"{code.lower()}.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in networks:
            f.write(f"    - {net}\n")