import dns.resolver

# 서브도메인 사전
with open("subdomain.txt") as file:
    subdomains = file.read().splitlines()

# DNS 요청을 보낼 도메인 (예: example.com)
target_domain = "testfire.net"

for subdomain in subdomains:
    full_domain = f"{subdomain}.{target_domain}"
    try:
        answers = dns.resolver.query(full_domain, "A")  # "A" 레코드 조회
        for answer in answers:
            print(f"Valid subdomain: {full_domain} => {answer}")
    except dns.resolver.NXDOMAIN:
        print(f"Invalid subdomain: {full_domain}")
    except dns.resolver.NoAnswer:
        pass
