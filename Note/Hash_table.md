## Hash_Table初步想法:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Hash%E8%A7%A3%E9%87%8B.png)

這張圖可以比較容易理解Hash table & hash Funtion

1.“菜瓜布”就是一個被丟進入的值，而必須先“將菜瓜布轉換成hash function看得懂的十進位”

2.透過管理員，也就是“Hash function”

3.找到菜瓜布所屬的位置，也就是“Hash table”，但是如果遇到需放置相同位置的值時，會產生碰撞collision，</br>可以用兩種方法解決 1.Open Addressing 2.Chaining (linked list)


## Hash Table功能：
主要的功能就是“加快搜尋速度”，尋找時，先找到key經MD5所轉換的bucket所屬位置，再從中的Link List尋找，省去了從頭搜尋（又稱為線性搜尋）的時間

## Hash Table 方法說明：
- add 
  - Listnode有空位，直接加入 
  - 沒空位，順著往下跑，加在linked-list最後

- delete 
  - 刪除點在第一個，直接刪除 
  - 刪除點不在第一個，要將前個數字游標指向刪除點的後一個

- contains 
  - Listnode內是空的，表示key不在table裡 
  - Listnode有值，如果cur.val = key，return True 
  - Listnode有值，如果cur.val != key，順著往下跑，看是否找到key

參考資料：演算法圖鑑，石田保輝 宮崎修一著，陳彩華譯

### Hash Function原理：
將key輸入funtionc後，透過演算法如：MD5(message digest algorithm)、SHA-1、SHA-2等，輸出固定長度且不規則的一串數值（稱為Hash Code），多以16進位表示，所得的不規則值也可視為數據的摘要，適用於告種狀況。

Hash Code雖然用16進位表示，但電腦內部都是以2進位來管理，也就是說，Hash Function在電腦內部一直進行著某種數值運算

#### feature： 

- 即使輸入非常大的數據（key長度不同），輸出數值的長度都一樣長

- 輸入相同的值，產生相同的輸出值，前提是利用同個演算法

- 即使輸入的數據很相似，輸出的結果差異很大

- 不可逆的，不能從輸出值反推key

- 演算法不同，計算方式也不同，即使輸入相同數據，Hash Code也不一樣

參考資料：演算法圖鑑，石田保輝 宮崎修一著，陳彩華譯

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Hash%20Table%E6%B5%81%E7%A8%8B%E5%9C%96.png)
