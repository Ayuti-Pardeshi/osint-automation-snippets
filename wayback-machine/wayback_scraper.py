import requests
import json
from collections import defaultdict
from urllib.parse import urlparse
from datetime import datetime

def get_wayback_urls(domain):
    print(f"[+] Querying Wayback Machine for {domain} ...")
    
    base_url = "http://web.archive.org/cdx/search/cdx"
    params = {
        "url": domain + "/*",
        "output": "json",
        "fl": "timestamp,original",
        "collapse": "urlkey"
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print(f"[-] Failed to fetch data. Status code: {response.status_code}")
        return {}

    data = response.json()
    headers = data[0]
    entries = data[1:]

    result = defaultdict(list)

    for entry in entries:
        timestamp, original_url = entry
        year = timestamp[:4]
        path = urlparse(original_url).path
        if path and path not in result[year]:
            result[year].append(path)

    return result

def save_to_json(domain, data):
    filename = f"{domain.replace('.', '_')}_wayback_data.json"
    with open(filename, "w") as f:
        json.dump({domain: data}, f, indent=2)
    print(f"[+] Saved data to {filename}")

if __name__ == "__main__":
    domain = input("Enter a domain (e.g. example.com): ").strip()
    wayback_data = get_wayback_urls(domain)
    if wayback_data:
        save_to_json(domain, wayback_data)
