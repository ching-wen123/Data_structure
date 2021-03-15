## Heap_Sort(堆疊排序法)
### 定義：
- Heap sort is a comparison based sorting technique based on Binary Heap data structure. </br>(一個基於二元堆疊排序的資料結構)
- It is similar to selection sort where we first find the maximum element and place the maximum element at the end.</br> We repeat the same process for remaining element.

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/heap_sort.png)

### 建立步驟：
- 將所有數儲存到堆疊中
- 取出root，與子結點相比較
- 重新排序
- 直到堆疊成遞降次序(descending order)

### 時間複雜度
- Best :O(n logn)
- Average :O(n logn)
- Worst :O(n logn)

## Merge_Sort
### 簡介:
- Merge sort is a "divide and conquer" algorithm.
- Divide the unsorted list into two sublists, until each containing only one element. 
- A list of one element is inherently sorted.
- last, conquer sublists then merge to one list
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Merge_sort%E6%93%8D%E4%BD%9C.png)

### 操作步驟：
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/merge_sort.png)

### 時間複雜度：
|              |Average Time   |Best Time         |Worst Time          |Extra Space        |Stability          |
|--------------|:-------------:|:----------------:|:------------------:|:-----------------:|:-----------------:|      
|Heap_Sort     |O(n logn)      |O(n logn)         |O(n log n)           |O(1)               |Unstable           |  
|Merge_Sort    |O(n logn)      |O(n logn)         |O(n log n)           |O(n)               |Stable           |  


- Best :O(n logn)
- Average :O(n logn)
- Worst :O(n logn)
