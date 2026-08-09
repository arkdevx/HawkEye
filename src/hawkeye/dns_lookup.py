import socket


def lookup(domain: str) -> None:
    domain = domain.strip()

    if not domain:
        print("\nError: Please enter a domain.")
        return

    try:
        addresses = socket.gethostbyname_ex(domain)

        print()
        print("DNS Lookup")
        print("-" * 30)
        print(f"Domain: {addresses[0]}")
        print(f"IP Addresses:")

        for ip_address in addresses[2]:
            print(f"  - {ip_address}")

    except socket.gaierror:
        print(f"\nCould not resolve domain: {domain}")