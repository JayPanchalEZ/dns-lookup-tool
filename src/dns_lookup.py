import dns.resolver
import re


# To validate if user has given a right domain name or not
def validate_domain(domain):
    # Regular expression to match a valid domain name
    domain_regex = r"^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$"
    return re.match(domain_regex, domain)

def dns_lookup(domain):
    print(f"\nDNS Records for {domain}: \n")
    
    # for A records
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        print("A Records (IP Addresses):")
        
        for record in a_records:
            print(f" - {record}")
            
    except dns.resolver.NoAnswer:
        print("No A records found.")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist. Enter a valid Domain Name.\n")
        return
        
    # For CNAME records
    try:
        cname_records = dns.resolver.resolve(domain, 'CNAME')
        print("\nCNAME Records:")
        
        for record in cname_records:
            print(f" - {record}")
            
    except dns.resolver.NoAnswer:
        print("\nNo CNAME records found.")
        
    # For MX Records
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print("\nMX Records (Mail Servers):")
        
        for record in mx_records:
            print(f" - {record}")
            
    except dns.resolver.NoAnswer:
        print("\nNo MX records found.")
        
if __name__ == '__main__':
    print("Welcome to the DNS Lookup Tool")

    while(True):
        
        domain = input("\nEnter a domain name (e.g., example.com): ").strip()
        
        if validate_domain(domain):
            dns_lookup(domain)
            break
        else:
            print("\nEnter a valid domain name! (e.g., example.com)")
        
    