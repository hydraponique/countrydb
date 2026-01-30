# Multi DB GeoIP Lists by Country

This repository contains **IP address ranges organized by country**, generated from Multi Geo DB repo: [ip-location-db by @sapics](https://github.com/sapics/ip-location-db) ***daily***. Each file corresponds to a country and contains a list of networks in CIDR notation.

---
## Databases

| Database | Countries | License | Updates | IPv4 |
|---|---|---|---|---|
| [GeoFeed + Whois + ASN](https://github.com/sapics/ip-location-db/tree/main/geo-whois-asn-country/) | [Link to Countries](https://github.com/hydraponique/countrydb/tree/main/output/geo-whois-asn-country/) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed) | Daily | [CSV](https://cdn.jsdelivr.net/npm/@ip-location-db/geo-whois-asn-country/geo-whois-asn-country-ipv4.csv)<br>[MMDB](https://cdn.jsdelivr.net/npm/@ip-location-db/geo-whois-asn-country-mmdb/geo-whois-asn-country-ipv4.mmdb) |
| [DB-IP Lite](https://github.com/sapics/ip-location-db/tree/main/dbip-country/) | [Link to Countries](https://github.com/hydraponique/countrydb/tree/main/output/dbip-country/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by [DB-IP](https://db-ip.com/) | Monthly | [CSV](https://cdn.jsdelivr.net/npm/@ip-location-db/dbip-country/dbip-country-ipv4.csv)<br>[MMDB](https://cdn.jsdelivr.net/npm/@ip-location-db/dbip-country-mmdb/dbip-country-ipv4.mmdb) |
| [DB-IP Lite + GeoFeed + Whois + ASN](https://github.com/sapics/ip-location-db/tree/main/dbip-geo-whois-asn-country/) | [Link to Countries](https://github.com/hydraponique/countrydb/tree/main/output/dbip-geo-whois-asn-country/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by [DB-IP](https://db-ip.com/) | Monthly | [CSV](https://cdn.jsdelivr.net/npm/@ip-location-db/dbip-geo-whois-asn-country/dbip-geo-whois-asn-country-ipv4.csv)<br>[MMDB](https://cdn.jsdelivr.net/npm/@ip-location-db/dbip-geo-whois-asn-country-mmdb/dbip-geo-whois-asn-country-ipv4.mmdb) |
| [GeoLite2](https://github.com/sapics/ip-location-db/tree/main/geolite2-country/) | [Link to Countries](https://github.com/hydraponique/countrydb/tree/main/output/geolite2-country/) | GeoLite2 License by [MaxMind](https://www.maxmind.com/) | Twice weekly | [CSV](https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-country/geolite2-country-ipv4.csv)<br>[MMDB](https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-country-mmdb/geolite2-country-ipv4.mmdb) |
| [GeoLite2 + GeoFeed + Whois + ASN](https://github.com/sapics/ip-location-db/tree/main/geolite2-geo-whois-asn-country/) | [Link to Countries](https://github.com/hydraponique/countrydb/tree/main/output/geolite2-geo-whois-asn-country/) | GeoLite2 License by [MaxMind](https://www.maxmind.com/) | Daily | [CSV](https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-geo-whois-asn-country/geolite2-geo-whois-asn-country-ipv4.csv)<br>[MMDB](https://cdn.jsdelivr.net/npm/@ip-location-db/geolite2-geo-whois-asn-country-mmdb/geolite2-geo-whois-asn-country-ipv4.mmdb) |

## Source

Data is downloaded from [ip-location-db by @sapics](https://github.com/sapics/ip-location-db) :

- Automaticly downloads the latest CSV file.
- Parses it into `.lst`, `.yaml`, `.mrs` files per country.
- Commits and pushes the updated files back to the repository.


## Usage

You can use these lists for:

- Firewall rules
- GeoIP-based routing
- IP filtering and analytics

Example: reading RU networks in Clash Mihomo:

```
  geoip-ru:
    type: http
    behavior: ipcidr
    format: mrs
    url: https://raw.githubusercontent.com/hydraponique/countrydb/main/output/dbip-country/ru.mrs
    path: ./rule-sets/geoip-ru.mrs
    interval: 86400
```
