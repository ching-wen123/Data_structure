## 目錄
- 時間複雜度Time Complexity
- O與Ω符號
- Sort排序
  - Bubble Sort(氣泡排序法)
  - Selection Sort(選擇排序法)
  - Insertion Sort(插入排序法)
  
### 時間複雜度Time Complexity
- O(1)
  - 不管你輸入多少個值，程式都會在同一個時間跑完
- O(n)
  - 執行步驟與輸入 n 等比例增加。例如當 n = 8，程式就會在 8 個步驟完成
- O(log n)
  - 當輸入的數量為 n 時，執行的步驟數會是 log n(log以2為底)例如：當 n = 4，程式會在 2 個步驟完成（4 = 2²）
- O(nlogn)
- O(n²)
- O(2^n)

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/time_complexity.png)
參考資料：https://medium.com/appworks-school/初學者學演算法-從時間複雜度認識常見演算法-一-b46fece65ba5

### O與Ω符號
- O符號：表示最壞情況下的運行時間。
- Ω符號：表示最好情況下的運行時間。

### Bubble Sort(氣泡排序法)
- 簡單的概念：我認為有點像是小學按身高排座位
  - 大家先任意的排成一列
  - 一開始將第一人與第二人進行比較，若第一個人高於第二個人，則交換位置
  - (第一個人與第二個人比較) 接著 (第二個人與第三個人比較)，所有人都排序一輪後，確定最後一個是最高的
  - 剔除最高的，重複上述步驟
  
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Bubble_Sort.png)

### Selection Sort(選擇排序法)
- 主要分為兩部分
  - 從「未排序中的數字」找到最小值
  - 將最小值放到「未排序好數列」的最左邊，並標示成已排序（這樣可以省去多創建一個arr的空間）
  - 重複上述兩個步驟，直到數列為ascending order

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Selection_Sort.png)

### Insertion Sort(插入排序法)
- 將資料分成已排序、未排序兩部份
- 依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置
- 插入時，由右向左比較，若已排序值>=正處理的值，則將處理值往右移，直到內部為小到大的狀態

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Insertion_sort.png)

### 時間複雜度比較
|               |Average Time          |Best Time       |Worst Time      |Stability     |
|---------------|:--------------------:|:--------------:|:--------------:|:------------:|                      
|Bubble Sort    |O(n ** 2)             |O(n)            |O(n ** 2)       |Stable        | 
|Selection Sort |O(n ** 2)             |O(n ** 2)       |O(n ** 2)       |Unstable      |       
|Insertion Sort |O(n ** 2)             |O(n)            |O(n ** 2)       |Stable        |   
