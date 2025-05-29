class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        i = 0 
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[i] = num
                i += 1
        return i
        
