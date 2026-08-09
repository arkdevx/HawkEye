from .dns_lookup import lookup
def main():
    while True:
        print()
        print("================================")
        print("          HawkEye 🦅")
        print("================================")
        print("Authorized OSINT & Security Toolkit")
        print()
        print("1. DNS Lookup")
        print("2. WHOIS Lookup")
        print("3. IP Information")
        print("4. HTTP Headers")
        print("5. SSL/TLS Information")
        print("0. Exit")
        print()

        choice = input("Select an option: ").strip()

        if choice == "0":
            print("\nGoodbye! 👋")
            break

        elif choice == "1":
            domain = input ("Enter domain: ")
            lookup(domain)

        elif choice == "2":
            print("\nWHOIS Lookup module — coming soon.")

        elif choice == "3":
            print("\nIP Information module — coming soon.")

        elif choice == "4":
            print("\nHTTP Headers module — coming soon.")

        elif choice == "5":
            print("\nSSL/TLS Information module — coming soon.")

        else:
            print("\nInvalid option. Please choose 0-5.")


if __name__ == "__main__":
    main()