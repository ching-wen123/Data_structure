## Codesignal
- CodeSignal is a skills-based assessment platform. 
- It can help you fimiliar with basic code and promote technical talent.

### My experience
- Through teacher's introduction, I started using this platfrom.
- It's not only recall my memory of python but also develop my skills level.

## Exercise
### EX1:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX1.png)
### Answer:
```python
if xs: (如果xs存在)
  res[0] = True(因為xs是存在的，所以會回傳True)
if xs[0]: (如果xs內容存在)
    res[1] = True(因為xs內容是不存在的，所以會回傳False)
```
### EX2:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX2.png)
### Answer:
題目要求：如果 "x ** Y" 大於L 且 小於等於R，return True</br>哪種方式最有效率
```python
if L < x ** y <= R:
  return True
else:
    return False
```
### EX3:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX3.png)
### Answer:
```python
a == (not b) # a 是不是 不是b，True
```

```python
not (a == b) # a是不是b，False，前面又一個“not”，所以變True
```

```python
a == not b 
```

```python
not a == b # 不是a 是不是 b，True
```
只有第三個與其他不同

### EX4:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX4.png)
### Answer:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX4_1.png)

"//" : 為取整數的意思</br>但若是除以負數且未能整除，將自動-1

### EX5:
求二進位
### Answer:

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX5.png)

### EX6:
if an int: 如果是整數，就會除以2，並取餘數(%)</br>
if not an int: 如果不是整數，則回傳-1
### Answer:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX6_1.png)
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX6_2.png)

### EX7:
圖片為如何操作排序一個arr</br>
比較簡單的方式為：直接呼叫python中的sorted，但題目要求利用遞迴一一檢查

![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX7_1.png)
### Answer:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX7_2.png)

### EX8:
透過“十進位轉十六進位”的方式，hex(int(n,x))
### Answer:
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/%E8%BD%89%E6%8F%9B%E8%A1%A8.png)
![](https://github.com/ching-wen123/ching-wen/blob/master/Image/EX8.png)
