## Shortest_path(Dijkstra)
### 定義：
固定其中一個頂點作為源節點然後找到該頂點到圖中所有其它節點的最短路徑，產生一個最短路徑樹。

### 細節說明：
- Dijkstra演算法的輸入包含了一個有權重的雙向圖 G，以及G中的一個來源頂點 S。
- 以 V 表示 G 中所有頂點的集合。
- 每一個圖中的邊，都是兩個頂點所形成的元素對。
- (u, v) 表示從頂點 u 到 v 有路徑相連。
- w(u, v) 表示從頂點 u 到頂點 v 的權重（weight），邊的權重可以想像成兩個頂點之間的距離。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Dijkstra%E6%B5%81%E7%A8%8B%E5%9C%96.png)

資料來源：https://zh.wikipedia.org/wiki/戴克斯特拉算法
