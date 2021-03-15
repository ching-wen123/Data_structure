def quicksort(list):#將一個list放入quicksort
    if len(list)<=1:#如果list的長度＝0，為一個空的list;若list=1，只有一個數無需比較
        return list
    smaller = []#創建空的list，利於與pivot比較完所放置
    equal = []
    bigger = []
    pivot = list[0]#選取其中一數作為pivot，開始比較

    for i in list:
        if i < pivot:
            smaller.append(i)#比較後，小於pivot的數放入smaller。但未知是否一次排序完畢，利用for迴圈
        elif i ==pivot:
                equal.append(i)
        else:
            bigger.append(i)#比較後，大於於pivot的數放入bigger

    return quicksort(smaller) + equal+ quicksort(bigger)#將三個list加總，得到排序後的數列
