import csv
import ipaddress
from collections import defaultdict
from pathlib import Path

INPUT_FILE = "dbip-geo-whois-asn-country-ipv4.csv"
OUTPUT_DIR = Path("geo/geoip")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

countries = defaultdict(list)

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    
    # Определяем, есть ли заголовок
    first_row = next(reader)
    try:
        # Пробуем преобразовать первый элемент в IP-адрес
        ipaddress.ip_address(first_row[0].strip())
        # Если получилось, значит это данные, а не заголовок
        f.seek(0)
        reader = csv.reader(f)
    except ValueError:
        # Если не получилось, значит это заголовок
        pass
    
    for row in reader:
        if len(row) < 3:
            continue
            
        ip_range_start = row[0].strip()
        ip_range_end = row[1].strip()
        country_code = row[2].strip().upper()
        
        if not country_code:
            continue
            
        try:
            start = ipaddress.ip_address(ip_range_start)
            end = ipaddress.ip_address(ip_range_end)
            
            # Преобразуем диапазон в CIDR блоки
            networks = ipaddress.summarize_address_range(start, end)
            
            for network in networks:
                countries[country_code].append(str(network))
                
        except (ValueError, ipaddress.AddressValueError):
            continue

# Запись в файлы
for code, networks in countries.items():
    clean_code = code.lower().replace(' ', '_').replace('-', '_')
    unique_networks = sorted(set(networks))
    
    # .lst файл
    lst_file = OUTPUT_DIR / f"{clean_code}.lst"
    with open(lst_file, "w", encoding="utf-8") as f:
        f.write("\n".join(unique_networks))
    
    # .yaml файл
    yaml_file = OUTPUT_DIR / f"{clean_code}.yaml"
    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for net in unique_networks:
            f.write(f"  - {net}\n")
