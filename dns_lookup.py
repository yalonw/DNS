import dns.resolver

my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']

ipval_cnt = {}
domain = 'google.com'

for i in range(10):
    result = dns.resolver.query(domain, 'A')    
    for ipval in result:
        ipval_text = ipval.to_text()

    if ipval.to_text() in ipval_cnt:
        cnt = ipval_cnt[ipval_text] + 1
        ipval_cnt[ipval_text] = cnt
    else:
        ipval_cnt[ipval_text] = 1
    
print(ipval_cnt)