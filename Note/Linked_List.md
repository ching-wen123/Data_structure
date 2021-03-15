## Linked List
### 定義：
Linked list(連結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，node會包含(1)data、(2)本身記憶體位置與(3)pointer指向下一個node的記憶體位置，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的最後一個node。

![](https://github.com/ching-wen123/ching-wen/blob/master/f2.png)


### Linked List ＆ Array 比較：
|      |Linked List                    |Array                      |
|------|:-----------------------------:|:-------------------------:|                   
|優點   |1.新增/刪除資料，調整pointer即可</br>2.記憶體位置不連續，適需求分配|利用index將資料存取|  
|缺點   |沒有index，查詢需走訪所有node     |1.若資料常改變，需時常調整矩陣大小</br>2.記憶體位置連續|

### 功能說明：
- 新增
- 刪除(去頭、去尾、走訪到中間特定Node進行刪除)
- 查詢（走訪所有Node）

### BlockChain
- Similar to single linked list, each block is connected to each other. 
- In Blockchain the flow of trace is opposite to single linked list. 
- Can trace back to the previous block all the way to the genesis block (first block of the chain) from the current block. 

相關補充影片：https://www.youtube.com/watch?v=WwfhLC16bis&feature=emb_title
