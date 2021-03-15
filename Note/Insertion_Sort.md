## Insertion Sort(插入排序法)
1.將資料分成已排序、未排序兩部份<br>2.依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置</br>3.插入時，由右向左比較，若已排序值>=正處理的值，則將處理值往右移，直到內部為小到大的狀態

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Insertion_sort.png)

## 時間複雜

|                 |Average Time              |Best Time            |Worst Time           |Stability          |
|-----------------|:------------------------:|:-------------------:|:-------------------:|:-----------------:|               
|Insertion Sort   |O(n**2)                   |O(1)                 |O(n**2)              |穩定(stable)        |  

