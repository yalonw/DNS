# DNS
Codes and Notes while learning DNS.  

### [問 DNS，拿 "www.google.com" 問 "8.8.8.8" 十次，統計他回傳的結果及他們出現的次數 ~](./dns_lookup.py)
> 提示：1. 一個 domain 可以有多筆 record 指向不同的 IP，所以才需要統計結果  
  　　　2. 可用 subprocess 搭配 nslookup


```
pip install dnspython
```

```python
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
```
### [為何 dns.resolver.query() 要透過 for loop 才能印出 IP addresses ??](./dns_trace_python_source_code.md)
