import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "Domain Name": w.domain_name,
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Name Servers": w.name_servers
        }
    except Exception:
        return "WHOIS lookup failed."

if __name__ == "__main__":
    domain = input("Enter domain: ")
    
    print("\n--- WHOIS Report ---\n")
    result = get_whois_info(domain)
    
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)
