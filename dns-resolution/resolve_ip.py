import socket

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Resolution failed."

if __name__ == "__main__":
    domain = input("Enter domain: ")
    print(f"IP Address: {resolve_domain(domain)}")
