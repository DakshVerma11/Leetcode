class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxand=max(nums)
        maxsubarr=1
        i=0
        while i+maxsubarr<len(nums):
            j=0
            while i+j<len(nums) and nums[i+j]==maxand:
                j+=1
            i+=j+1 
            maxsubarr=max(maxsubarr,j)
        return maxsubarr
