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

|                 |Average Time              |Best Time            |Worst Time           |Stability          |
|-----------------|:------------------------:|:-------------------:|:-------------------:|:-----------------:|               
|Heap Sort        |O(n logn)                 |O(n logn)            |O(n logn)            |不穩定(Unstable)     |  


相關補充影片https://www.youtube.com/watch?v=MtQL_ll5KhQ&feature=emb_title
