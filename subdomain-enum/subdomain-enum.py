
import subprocess
import json
import sys

def run_sublister(domain):
    try:
        print(f"[+] Running Sublist3r for {domain}...\n")

        result = subprocess.run(
            ["sublist3r", "-d", domain, "-o", "temp_output.txt"],
            capture_output=True,
            text=True
        )

        with open("temp_output.txt", "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]

        return subdomains

    except FileNotFoundError:
        print("[-] Sublist3r is not installed.")
        sys.exit(1)

def save_to_json(domain, subdomains):
    filename = f"{domain.replace('.', '_')}_subdomains.json"
    data = {
        "domain": domain,
        "subdomains": subdomains,
        "count": len(subdomains)
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n[+] Results saved to {filename}")

if __name__ == "__main__":
    domain = input("Enter domain: ").strip()
    subdomains = run_sublister(domain)

    if subdomains:
        save_to_json(domain, subdomains)
    else:
        print("[-] No subdomains found.")
