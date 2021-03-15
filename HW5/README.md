## BFS
### 簡介：
- 系統地展開並檢查圖中的所有節點，以找尋結果。
- 換句話說，它並不考慮結果的可能位址，而是徹底地搜尋整張圖，有找到則回傳True，沒找到則回傳False。
- 實作的部分是從根節點開始，沿著樹的寬度遍歷樹的所有節點。若所有節點均被存取，則演算法中止。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/BFS.png)

### 程式碼：
```python
from collections import defaultdict 
  
class Graph:    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        answer = []
        queue = [s]
        visited = defaultdict(list)    #visited必須先被定義，才能給值
        visited[s] = True
        #while queue is not None:
        #while queue != None:
        while queue:                #如果queue內有值
            vertex = queue.pop(0)
            answer.append(vertex)
            for i in self.graph[vertex]:
                if visited[i] is not True:   
                    visited[i] = True
                    queue.append(i)
            #print(answer)
            #print(queue)
            #print(id(queue))
        return answer
```
## DFS
### 簡介：
- 沿著樹的深度遍歷樹的所有節點，儘可能的搜尋樹的分支。
- 當節點(v)的所在邊都已被探尋過，搜尋將回溯到節點(v)，重新另一條邊的搜尋，過程一直進行到節點(v)可到達的所有節點都走訪為止。
- 如果還存在未發現的節點，則選擇其中一個作為新節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/DFS.png)

### 程式碼：
```python
from collections import defaultdict 
  
class Graph:    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def DFS(self, s):
        answer = []
        stack = [s]
        visited = defaultdict(list)    #visited必須先被定義，才能給值
        visited[s] = True
        while stack:                #如果queue內有值
            vertex = stack.pop()
            answer.append(vertex)
            for i in self.graph[vertex]:
                if visited[i] is not True:   
                    visited[i] = True
                    stack.append(i)
            #print(answer)
            #print(queue)
            #print(id(queue))
        return answer
```
## DFS & BFS比較：
|              |DFS                            |BFS                        |
|--------------|:-----------------------------:|:-------------------------:|                   
|實現方式       |Queue                          |Stack                      |  
|頂點選擇方式    |FIFO(先進先出)                  |LIFO(後進先出)               |
|搜尋順序       |優先搜尋距離頂點較近的點，當同距離遍歷結束，再往下個距離層級搜尋)|單一路徑往下探查，直到無法繼續前進，折返下一個路徑|
|花費記憶體空間  |需要與狀態數成正比的記憶體空間，較沒效率，無法快速找到目標點|需要與遞迴深度成正比的記憶體空間，遞迴深度不需佔用較大的記憶體|
|優點          |解決最短路徑問題                 |解決連通性問題                 |
|缺點          |必須遍歷所有節點                 |如果路徑較長，需花費長時間找目標  |
|空間複雜度     |O（v）                         |O（v）                       |

