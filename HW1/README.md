## Quick Sort
### 簡介
1.從數列中挑選一數當作基準值(PIVOT)</br>2.分割，調整數列，左邊的數為“小於”PIVOT，右邊的數為“大於”PIVOT</br>3.將左邊小於PIVOT的數視為「新的數列」，右邊大於PIVOT的數視為「另一個新的數列」，重複上述分割的動作，直到每個數值都是獨立一個(不能再分出新數列)

![](https://github.com/ching-wen123/ching-wen/blob/master/f1-2.png)

### 流程圖
![](https://github.com/ching-wen123/ching-wen/blob/master/HW1/quick_sort%E6%B5%81%E7%A8%8B%E5%9C%96.png)

### 時間複雜度
|              |Average Time   |Best Time         |Worst Time          |Extra Space        |Stability          |
|--------------|:-------------:|:----------------:|:------------------:|:-----------------:|:-----------------:|      
|Quick_Sort    |O(n logn)      |O(n logn)         |O(n ** 2)           |O(n)               |Unstable           |  


