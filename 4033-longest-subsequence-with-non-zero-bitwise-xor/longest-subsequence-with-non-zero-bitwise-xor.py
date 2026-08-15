class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        totalXOR=0
        totalOR=0
        for num in nums:
            totalXOR^=num
            totalOR|=num
        
        if not totalXOR and not totalOR:
            return 0
        elif not totalXOR:
            return len(nums)-1
        else:
            return len(nums)