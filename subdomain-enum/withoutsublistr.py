
---

# Option 2 — Pure Python (Without Sublist3r)

If you want something cleaner and more independent, use passive certificate transparency logs.

Example using crt.sh:

```python
import requests
import json

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    subdomains = set()

    for entry in data:
        name = entry.get("name_value")
        if name:
            subdomains.update(name.split("\n"))

    return list(subdomains)

if __name__ == "__main__":
    domain = input("Enter domain: ").strip()
    subs = get_subdomains(domain)

    output = {
        "domain": domain,
        "subdomains": subs,
        "count": len(subs)
    }

    filename = f"{domain.replace('.', '_')}_crt_subdomains.json"

    with open(filename, "w") as f:
        json.dump(output, f, indent=4)

    print(f"[+] Saved to {filename}")
