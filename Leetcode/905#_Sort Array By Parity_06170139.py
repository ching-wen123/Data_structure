class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even =[]
        for i in A:
            if i % 2 == 0: #even
                even.append(i)
            else:   #i % 2 != 0: #odd
                odd.append(i)
        return even + odd