## Binary_search_tree
### search:
必須進行比較，碰到相等就是找到目標，比較後較小的往左走，比較後較大的往右走，走到盡頭就結束。</br> ➡️利用遞迴重複比較 target 與 root 比較 root要持續往下跑，與target比較。

 case1 : root不存在，根本找不到，return none

 case2 : root存在，等於target，return root

 case3 : root存在，root > target，往左比較

 case4 : root存在，root < target，往右比較 

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/search_node.png)
### Delete:
case1 : 若無子節點，刪除目標節點即可。

case2 : 刪除帶有一個子節點時，“有右節點，無左節點”，直接刪除

case3 : 刪除帶有一個子節點時，“有左節點，無右節點”，必須考慮重複值的狀況。</br>若重複：重新呼叫self.delete(root.left,target)，若無重複：直接刪除 

case4 : 刪除帶有兩個子節點時degree = 2，先刪除目標節點，再從被刪除的左子樹，找出最大值取代刪除值，或從右子樹找出最小值取代。

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/delete_node.png)
### Insert:
利用遞迴的方式，知道新增的值應該在哪加入 think</br>➡️當前節點爲空時，說明應該將「插入節點」插入到上一個遍歷節點的左子節點或右子節點。

case1 : root沒有值，直接將值賦予root

case2 : root有值且"大於"val，右左比較，但沒有左節點，val = root.left 

case3 : root有值且"大於"val，右左比較，仍有左節點，self.insert(root.left,val)

case4 : root有值且"小於"val，向右比較，但沒有右節點，val = root.right 

case5 : root有值且"小於"val，向右比較，有右節點，self.insert(root.right,val)

case6 : root有值且root = val，新增在root的左節點

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/insert_node.png)
## Modify:
先利用delete功能，再利用insert功能 

(1.) delete，需判斷無節點、有左節點、有右節點、有二個節點的狀況 

(2.)重新整理樹狀後 

(3.) insert，需與root比較，決定向右走(val > root.val)、向左走(val <= root.val)

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/modify_node.png)
