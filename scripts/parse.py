import csv
import gzip
import ipaddress
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
        if not country_code or not network:
            continue
        try:
            net_obj = ipaddress.ip_network(network, strict=False)
        except ValueError:
            continue
        countries[country_code].append(str(net_obj))

for code, networks in countries.items():
    lst_file = OUTPUT_DIR / f"{code.lower()}.lst"
    with open(lst_file, "w", encoding="utf-8") as f:
        f.write("\n".join(networks))

    yaml_file = OUTPUT_DIR / f"{code.lower()}.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in networks:
            f.write(f"    - {net}\n")
