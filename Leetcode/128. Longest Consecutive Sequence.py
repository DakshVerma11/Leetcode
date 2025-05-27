class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #memory exceeded not optimal
        if not nums:
            return 0
        min_val=min(nums)
        marker = ['0'] * (max(nums)-min_val+1) 
        
        for x in set(nums):
            marker[x - min_val] = '1'
        
        marker_str = "".join(marker)
        
        blocks = marker_str.split('0')
        
        return max((len(block) for block in blocks))






class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        longest=0
        for n in numset:
            if n-1 not in numset:
                current = n
                curlen = 0

                while n in numset:
                    curlen+=1
                    n+=1

                longest=max(longest,curlen)

        return longest
