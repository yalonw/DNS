# DNS
Codes and Notes while learning DNS.  

### 問 DNS，拿 `www.google.com` 問 `8.8.8.8` 十次，統計他回傳的結果及他們出現的次數 ~
> 提示：1. 一個 domain 可以有多筆 record 指向不同的 IP，所以才需要統計結果  
  　　　2. 可用 subprocess 搭配 nslookup

#### [題目寫啥看不懂 QAQ，點這先瞭解一下...](./what_is_dns.md)
#### [寫好了~ 開心 ヽ(✿ﾟ▽ﾟ)ノ](./dns_lookup.py)
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
</br>

### [為何 dns.resolver.query() 要透過 for loop 才能印出 IP addresses ??](./dns_trace_python_source_code.md)

#### **簡單來說**  [(點這看詳細)](./dns_trace_python_source_code.md)
1. 因為 `Answer(object)` 沒有 override `__str__`  
   所以 `print(Answer())` 會印出 `object` 的 `__str__`  

1. 若 `print(Answer().rrset)` 會呼叫 `RRset` 的 `__str__ `  
   則會印出 「`google.com. 111 IN A 216.58.200.238`」 

1. 因為 `Answer()` 有 override `__iter__`  
   所以 [ `x for x in Answer()` ] 等於 [ `x for x in Answer().rrset` ]  
   `type(rrset) == RRset`    

1. 又因為 `RRset` 繼承 `Rdataset` 繼承 `Set`，而 `Set()` 有 override `__iter__`  
   所以 [ `x for x in Answer().rrset` ] 等於 [ `x for x in Answer().rrset.items` ]  

1. 而 `Set()` 在 `__init__` 有 assign `self.items = []`   
   表示 items 的資料型態是 list，所以才需要使用 **迴圈**，用 for loop `print()` 出來

</br>

### 其他筆記：[DNS Messages Format](./dns_message_format.md)
![DNS message packet](./DNS%20message%20format.png)
