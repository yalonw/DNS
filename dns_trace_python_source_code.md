#####  Date : 6 January 2020
# 為何 dns.resolver.query() 要透過 **for loop** 才能印出 IP addresses ??
  
## **查詢 DNS 的代碼**  

> 參考資料：https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm  

In the below program we find the ip address for the domain using the dns.resolver method. Usually this mapping between IP address and domain name is also known as 'A' record.  

```python 
import dns.resolver

domain = 'google.com'
result = dns.resolver.query(domain, 'A')
for ipval in result.rrset:
    print(ipval.to_text())
```
When we run the above program, we get the following output ~  

```Shell
216.58.200.238
```  
</br>

---------------------
## **我拆解研究一下**  

1. 透過 [`dns.resolver.`query`()`](http://www.dnspython.org/docs/1.15.0/dns.resolver-pysrc.html#query) <sup>1</sup> 來找 IP addresses

1. 這裡的 `query` <sup>1</sup> 會 [`return get_default_resolver().`query`()`](http://www.dnspython.org/docs/1.15.0/dns.resolver-pysrc.html#Resolver.query) <sup>2</sup> 

1. 這裡的 `query` <sup>2</sup> 會 `return answer` ，且 `answer = Answer()` 

1. 再往下尋找會找到 [`class `Answer`(object)`](http://www.dnspython.org/docs/1.15.0/dns.resolver-pysrc.html#Answer)

1. 但是！ `class Answer(object)` 沒有定義 `__str__` ，所以 `print(result)` 出來的東西會是 *`object`* 所定義的 `__str__`，因為 `Answer` 繼承 `object` ，但... 這不是我們要的答案 QAQ

```python 
domain = 'google.com'
result = dns.resolver.query(domain, 'A')
print(result)
```
```Shell
# output
<dns.resolver.Answer object at 0x0329BD18>
```
6. 不過！ `class Answer(object)` 有定義 `__iter__` ，所以可以透過 for loop 來 `iterate Answer`，相當於 `iterate Answer.rrset` <sup>3</sup> ， `print()` 出來的 [代碼和結果如上上上](#查詢DNS的代碼) ~  
>　**Class Answer 的註釋 <sup>3</sup>：**   
For convenience, the answer object implements much of the sequence protocol, forwarding to its **rrset**.  
E.g. *" for a in answer "* is equivalent to *" for a in answer.rrset "*,
     *" answer [ i ] "* is equivalent to *" answer.rrset [ i ] "*, and 
     *" answer [ i : j ] "* is equivalent to *" answer.rrset [ i : j ] "*.

> 備註：大大說 iterate Answer 實際上可視為 iterate Answer 物件的 attribute-rrset，因為 class Answer 裡面有 rrset 這個變數 variables，所以 rrset 就是他的 attribute 之一...   懂嗎? 我是不懂啦 (╥﹏╥)

-------------------
### **再拆細一點**

7. 在 `class Answer(object)` 中， [`def __iter__(self)`](http://www.dnspython.org/docs/1.15.0/dns.resolver-pysrc.html#Answer.__iter__) 會 [`return self.`rrset` and iter(self.`rrset`) or iter(tuple())`](http://www.dnspython.org/docs/1.15.0/dns.rrset-pysrc.html) 

1. OK! 從這裡看到， for  loop `print()` 出來的是 `rrset` 

1. 但... 直接 `print(result.rrset)` 除了 IP addresses 還多了其他東西 QAQ

```python 
domain = 'google.com'
result = dns.resolver.query(domain, 'A')
print(result.rrset)
```
```Shell
# output
google.com. 111 IN A 216.58.200.238
```
---------------------
### **再再拆細一點**

10. 可以發現 [`rrset`](http://www.dnspython.org/docs/1.15.0/dns.rrset-module.html) 來自 [`class RRset()`](http://www.dnspython.org/docs/1.15.0/dns.rrset.RRset-class.html) ，而 [`RRset`](http://www.dnspython.org/docs/1.15.0/dns.rrset.RRset-class.html) 繼承 [`Rdataset`](http://www.dnspython.org/docs/1.15.0/dns.rdataset.Rdataset-class.html) ， [`Rdataset`](http://www.dnspython.org/docs/1.15.0/dns.rdataset.Rdataset-class.html) 繼承 [`Set`](http://www.dnspython.org/docs/1.15.0/dns.set.Set-class.html) ，如下圖~

```
   object --+        
            |        
      set.Set --+    
                |    
rdataset.Rdataset --+
                    |
                   RRset
```
11. 在 `class Set(object)` 中， [`def __iter__`](http://www.dnspython.org/docs/1.15.0/dns.set-pysrc.html#Set.__iter__) 會 `return iter(self.items) `，而 *`self.items`* 在 [`def __init__`](http://www.dnspython.org/docs/1.15.0/dns.set-pysrc.html#Set.__init__) 裡有 assign 一個空的 **list** -->「`self.items = [] `」，所以 *`self.items`* 的資料型態是一個 `list` 

12. 然後！！！ 通過各種繼承， `rrset` 因此是一個 **list** 的資料型態！！！  而要把 list 裡面的 element 走過一遍並印出來，就需要使用 **迴圈**，所以才用 for loop `print()` 出來

> 備註：但... 為啥 for loop 印出來的時候，只剩下 IP addresses `( 216.58.200.238 )` ??   
  　　　其他東西 `( google.com. 111 IN A )` 去哪了 ??

---------------------------
### **再再再拆細一點吧 (⋟﹏⋞)**

13. 在 `class RRset()` 中， `def __str__` 會 `return self.to_text()` ，而在 [`def `to_text`()`](http://www.dnspython.org/docs/1.15.0/dns.rrset-pysrc.html#RRset.to_text) 中可以看到他 `return` 時，會再加入 *`self.name`*

1. 而 `class Rdataset()` ，則在 [`return `to_text`(): `](http://www.dnspython.org/docs/1.15.0/dns.rdataset-pysrc.html#Rdataset.to_text)  時加入 *`self.ttl, dns.rdataclass.to_text(rdclass), dns.rdatatype.to_text(self.rdtype)`*

```python
class RRset(dns.rdataset.Rdataset):
        ...
    def __str__(self): 
        return self.to_text() 
        ...
    def to_text(self, origin=None, relativize=True, **kw):
        return super(RRset, self).to_text(self.name, origin, relativize, 
                                          self.deleting, **kw)
        ...
```

15. 所以， `print(Rdataset)` 會是「`ttl + rdclass + rdtype + IP addresses`」；而 `RRset` 繼承 `Rdataset` ，`print(RRset)` 就會呈現「`self.name + ttl + rdclass + rdtype + IP addresses`」

> 備註：在代碼上要打 `print(result.rrset)` ，上面的 `print(Rdataset)` 和 `print(RRset)` 是理解用的

```Shell
google.com. 111 IN A 216.58.200.238

# google.com.    -> name ──────────────────────────────────────────+
# 111            -> ttl  ───────────────────────+                  │ class RRset
# IN             -> rdclass                     │ class Rdataset ──+       to_text()
# A              -> rdtype                      │       to_text()
# 216.58.200.238 -> IP addresses ── class Set ──+
```
</br>

---------------------------
## **哦 ~ 所以簡單來說 ~~**  
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


> 備註：但... 但... 在 `class Set()` 裡，把 **誰** 塞進 *`items`* 了呀 ??  
  　　　list of what ??  
  　　　從哪兒知道他會把 IP addresses 塞進去呀 ???　 ˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚

-----------
### **回頭檢查一下** QAQ

- 在 `class Set()` 我沒找到喵 Orz
- 但在上一層的 [`class Rdataset()`](http://www.dnspython.org/docs/1.15.0/dns.rdataset-pysrc.html#Rdataset) 看到他說：  
*" DNS rdatasets ( an rdataset is a set of `rdatas` of a given type and class ) "*
- 所以應該和 `rdatas` 有關吧 ???!!

</br>
 

 ⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠ 大大求解  ⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠⎝༼ ◕Д ◕ ༽⎠ 