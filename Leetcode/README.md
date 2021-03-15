## Leetcode
- It’s a website where can practice coding skills. 
- There are 800+ questions even more, each with multiple solutions and discussions
- It's good for sloving questions but not limit my thinking
- Questions are ranked by level of difficulty: easy, medium, and hard.
- Choose the questions depends on your level.

## Title:

|題數  |題目                   |解答                     |難易度                     |
|------|:--------------------:|:----------------------:|:------------------------:|                     
|27  |[Remove Element](https://leetcode.com/problems/remove-element/)|[answer](https://github.com/ching-wen123/ching-wen/blob/master/Leetcode/27%23_Remove%20Element_06170139.py)|Easy                 |  
|283 |[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|[answer](https://github.com/ching-wen123/ching-wen/blob/master/Leetcode/283%23_Move%20Zeroes_06170139.py)|Easy           | 
|700 |[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[answer](https://github.com/ching-wen123/ching-wen/blob/master/Leetcode/700%23_Search%20in%20a%20Binart%20Search%20Tree_06170139.py)|Easy           | 
|136 |[Single Number](https://leetcode.com/problems/single-number/)|[answer](https://github.com/ching-wen123/ching-wen/blob/master/Leetcode/136%23_Single%20Number_06170139.py)|Easy 
|905 |[Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/submissions/)|[answer](https://github.com/ching-wen123/ching-wen/blob/master/Leetcode/905%23_Sort%20Array%20By%20Parity_06170139.py)|Easy  




### 27_Remove Element
- 題目：</br>
給定arr，並將arr中特定val刪除。

- 我的解答：</br>
第一次寫的時候，沒有想到“連續出現val”的狀況，只要每檢查一個數index加一，但當第一個重複值刪除後，下個數的index會自動補上，所以只有當不等於val時，index才加一。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leed27_1.png)

以下為正確執行結果 :smile:

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leed27_2.png)

### 283_Move Zeroes
- 題目：</br>
給定arr，並將arr中的0移至arr最後端，保持0以外的數是由小到大排序的。

- 我的解答：</br>
一開始我的想法是當遇到0，即pop(0)，並將arr.append(0)，結果如下，但我的while沒寫好，變成只要有0都會pop，導致錯誤。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet283_1.png)

後來我想到python中有個count語法，就嘗試用arr.count(0)，以這個當作我要append(0)的基準，結果如下。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet283_2.png)

我本想說應該沒問題了吧，結果還是有錯，我就上網再次確認"pop"的用法，我才恍然大悟"pop" & "remove"的差異，最後結果如下。
參考之料：https://blog.csdn.net/xavierri/article/details/78591259

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet283_3.png)

### 700_Search in a Binary Search Tree
- 題目：</br>
透過BST中search功能，找到題目要求的val

- 我的解答：</br>
這題其實蠻簡單的，因為跟HW3的作業是一樣的，我就回想一下search中可能的狀況，分為4個
  - root不存在
  - root == val(目標)
  - root > val(目標)，透過“遞迴”，讓root往左下移動，直到root == val
  - root == val(目標)透過“遞迴”，讓root往右下移動，直到root == val

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet_700.png)


### 136_Single Number
- 題目：</br>
找出arr中唯一的值

- 我的解答：</br>
一開始我想到的是創建一個answer=[]，從nums中每讀取到一個數字，就新增進answer，若已經存在這個數就從answer中刪除

```python
for i in nums:
  if i not in answer:   #若answer中沒有該數字，就新增進answer
      answer.append(i)
   else:
       answer.pop(0)   #若已經存在這個數就從answer中刪除
 return answer
```
結果如下：
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet136_1.png)

看樣子感覺對了，只要改return answer[0]，結果如下
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet136_2.png)

結果還是錯了，Leetcode給了我一個測資是[4,1,2,1,2]，差別在於這個singal number出現在第一個，所以整個判斷過程不應該被刪除，但"answer.pop(0)"，讓我的第一個數字(4)被刪除了，應該要改成"answer.remove(i)"，指定我要刪除的數字而不是位置


### 905_Sort Array By Parity
- 題目：</br>
排序arr，將偶數放在arr前，奇數放在arr後

- 我的解答：</br>
我的想法很簡單但也很浪費空間，我創了odd & even的arr，接著判斷若是odd則放入該arr，最後依題目要求，return even+odd

```python
odd = []
even = []
for i in A:
    if i % 2 == 0:   #除以2沒有餘數，肯定為偶數
        even.append(i)
    else:
        odd.append(i)
 return even + odd
```

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/Leet_905.png)
