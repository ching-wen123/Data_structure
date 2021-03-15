class Solution():
    def maxheapify(self,arr,length,i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < length and arr[largest] < arr[left]:
            largest = left
        if right < length and arr[largest] < arr[right]:
            largest = right
            
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            Solution().maxheapify(arr, length, largest)
    def heapbuild(self, arr,length):
        lenght = len(arr)
        leftt = int((length / 2) -1)             
        while leftt >= 0:                 
            Solution().maxheapify(arr, length, leftt)
            leftt -= 1 
    def heap_sort(self, arr):
        length = len(arr)
        Solution().heapbuild(arr,length)
    
        while length < 2:
            arr[0], arr[length - 1] = arr[length - 1], arr[0]
            length -= 1
            Solution().maxheapify(arr, length, 0)
        return arr

list = [3,6,9,11,43,2,1]
Solution().heap_sort(list)
list
