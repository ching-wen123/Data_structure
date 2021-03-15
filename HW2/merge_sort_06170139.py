class Solution(object):
    def merge_sort(self, List):
         if len(List) <= 1:
            return List
         if len(List) > 1:
            middle = len(List) // 2
            left = List[:middle]
            right = List[middle:]
            Solution().merge_sort(left)
            Solution().merge_sort(right)
            
            left_point = 0
            right_point = 0
            index = 0
            while left_point < len(left) and right_point < len(right):
                if left[left_point] < right[right_point]:
                    List[index] = left[left_point]
                    left_point += 1
                else:
                    List[index] = right[right_point]
                    right_point += 1
                index += 1
            while left_point < len(left):
                List[index] = left[left_point]
                left_point += 1
                index += 1
            while right_point < len(right):
                List[index] = right[right_point]
                right_point += 1
                index += 1
            return List




list = [3,6,9,11,43,2,1]
Solution().merge_sort(list)
list