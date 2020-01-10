###### Date : 6 January 2020

## DNS Messages Format

```
type(result.response)
<class 'dns.message.Message'>
```
#### 程式碼如下：
```python 
domain = 'google.com'
result = dns.resolver.query(domain, 'A')
print(result.response)
```
```Shell
# output

id 52066
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
google.com. IN A
;ANSWER
google.com. 235 IN A 216.58.200.238
;AUTHORITY
;ADDITIONAL
```

### [DNS message packet](./DNS%20message%20format.png)

|     |  |  |
| :-: | :---------: | :-------------- |
|  1  | Header      | { ID, Flag, Question count, Answer count, Authority count, Additional count } | 
|     |             |  → Flag：{ OR, OpCode, AA, TC, RD, RA, Z, AD, XD, RDode }                     |
|     |  |  |
|  2  | Question    | { DNSname, TYPE, CLASS }                                                      |
|  3  | Answer      | { DNSname, TYPE, CLASS, TTL, (RDATA_LENGTH), RDATA }                          |
|  4  | Authority   |  | 
|  5  | Additional  |  | 


#### 參考資料：
 + [Protocol and Format : DNS Messages](http://www-inf.int-evry.fr/~hennequi/CoursDNS/NOTES-COURS_eng/msg.html)  
 + [網域名稱系統 | 翻轉工作室-粘添壽](http://www.tsnien.idv.tw/Internet_WebBook/chap13/13-6%20DNS%20%E8%A8%8A%E6%81%AF%E6%A0%BC%E5%BC%8F.html)  
 + [筆記一下學習網路五層#2.5 | Ben the dust](https://ithelp.ithome.com.tw/articles/10210481)  
