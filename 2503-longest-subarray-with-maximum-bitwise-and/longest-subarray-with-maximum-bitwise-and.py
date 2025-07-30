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
        
        
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxand = max(nums)
        max_len = current_len = 0
        
        for num in nums:
            if num == maxand:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        
        return max_len



class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxval = max(nums)
        return max(len(list(group)) for key, group in groupby(nums) if key == maxval)
