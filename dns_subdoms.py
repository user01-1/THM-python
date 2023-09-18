import dns.resolver

# subdomain wordlist
with open("subdomain.txt") as file:
    subdomains = file.read().splitlines()

# DNS request
target_domain = "example.com"

for subdomain in subdomains:
    full_domain = f"{subdomain}.{target_domain}"
    try:
        answers = dns.resolver.query(full_domain, "A")  # "A" record
        for answer in answers:
            print(f"Valid subdomain: {full_domain} => {answer}")
    except dns.resolver.NXDOMAIN:
        print(f"Invalid subdomain: {full_domain}")
    except dns.resolver.NoAnswer:
        pass
