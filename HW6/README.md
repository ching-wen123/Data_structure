## Minimum Spanning Tree(Kruskal)
### 定義： 
Kruskal為最小生成樹的其中一種演算法，而圖中若存在相同權重的邊也有效的。

- 簡單的例子
  - 頂點看做“城市”，邊看做連接每個城市的“通訊網”，邊的權重看作“連接城市通訊線的最小成本”
  - 根據最小生成樹建立的通訊網，就是城市之間最低成本的通訊網
  
### 細節說明： 
- 將原圖中所有的邊按權重從小到大排序 
- 從權重最小的邊開始搜尋，如果這條邊連接的兩個節點，不屬於同個根節點，則添加這條邊到圖G中
- 重複2.的步驟，直到n個點形成n-1個邊，即形成最小生成數

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/MST%E6%B5%81%E7%A8%8B%E5%9C%96.png)

- 重要規則：
  - 不能形成cycle
  - 圖形是可以連接的

## Shortest Path(Dijkstra)
### 定義：
固定其中一個頂點作為源節點然後找到該頂點到圖中所有其它節點的最短路徑，產生一個最短路徑樹。

### 細節說明：
- Dijkstra演算法的輸入包含了一個有權重的雙向圖 G，以及G中的一個來源頂點 S。
- 以 V 表示 G 中所有頂點的集合。
- 每一個圖中的邊，都是兩個頂點所形成的元素對。
- (u, v) 表示從頂點 u 到 v 有路徑相連。
- w(u, v) 表示從頂點 u 到頂點 v 的權重（weight），邊的權重可以想像成兩個頂點之間的距離。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Dijkstra%E6%B5%81%E7%A8%8B%E5%9C%96.png)

資料來源：https://zh.wikipedia.org/wiki/克鲁斯克尔演算法

資料來源：https://zh.wikipedia.org/wiki/戴克斯特拉算法
