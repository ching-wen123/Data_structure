class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        answer = []
        for i in nums:
            if i not in answer:
                answer.append(i)
            else:    #answer中出現過該數字
                answer.remove(i)
        return answer[0]