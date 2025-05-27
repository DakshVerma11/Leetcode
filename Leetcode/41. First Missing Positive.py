class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        i=1
        while True:
            if i not in numset:
                return i
            i+=1
