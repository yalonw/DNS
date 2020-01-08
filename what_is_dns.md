###### Date : 8 January 2020

## 名詞解釋
- [**DNS**](https://zh.wikipedia.org/wiki/%E5%9F%9F%E5%90%8D%E7%B3%BB%E7%BB%9F)  
  網域名稱系統（Domain Name System）是將人們可讀取的網址 Domain Name 轉換為機器可讀取的 IP Address。  
  DNS Server 的工作原理類似電話簿，管理名稱和數字之間的映射關係。  
> 參考資料：  
  簡單瞭解請看： [Amazon 解釋什麼是 DNS？](https://aws.amazon.com/tw/route53/what-is-dns/)  
  詳細瞭解請看： [DNS Server 是什麼？如何運用？](https://www.stockfeel.com.tw/dns-%E4%BC%BA%E6%9C%8D%E5%99%A8%E6%98%AF%E4%BB%80%E9%BA%BC%EF%BC%9F%E5%A6%82%E4%BD%95%E9%81%8B%E7%94%A8%EF%BC%9F/)

- [**Domain** (Name)](https://zh.wikipedia.org/wiki/%E5%9F%9F%E5%90%8D)  
  網址/網域名稱是 IP 位址的代稱，目的是為了便於記憶，例如 `www.google.com`。

- [**IP Address**](https://zh.wikipedia.org/wiki/IP%E5%9C%B0%E5%9D%80)  
  IP 位址就像住宅地址一樣，可以標識傳送和接收資料的位置。  
  而所有連線到網際網路的網站和裝置都有獨特的 IP 位址，例如我查 Google 的 IP Address 是 `216.58.200.238`。
> 參考資料：  
  簡單瞭解請看： [Google 解釋什麼是 IP 位址？](https://support.google.com/wifi/answer/6246678?hl=zh-HK)  

- **`8.8.8.8`**  
  是 [Google Public DNS](https://zh.wikipedia.org/wiki/Google_Public_DNS)， 是 Google 對大眾推出的公共免費域名解析服務。  

</br>

## 解讀題目...  
題目：「問 DNS，拿 `www.google.com` 問 `8.8.8.8` 十次，統計他回傳的結果及他們出現的次數 ~」  
- DNS Server IP = `8.8.8.8` ----> [code 參考資料](https://stackoverflow.com/questions/3898363/set-specific-dns-server-using-dns-resolver-pythondns)
- Domain = `www.google.com`  
- 尋找 IP Address ---------------> [code 參考資料](https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm)
  + 這裡找的 IP 類型是「 IPv4 位址記錄 ( A )」，其他 DNS record type 請見[維基百科](https://zh.wikipedia.org/wiki/DNS%E8%AE%B0%E5%BD%95%E7%B1%BB%E5%9E%8B%E5%88%97%E8%A1%A8)
- 找 IP 的動作重複十次
- 紀錄 IP Address 有沒有不一樣
