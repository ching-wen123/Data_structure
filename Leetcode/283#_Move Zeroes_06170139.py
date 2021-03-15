class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        nums.count(0) #計算nums中出現幾次0
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums