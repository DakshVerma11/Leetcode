class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxval = max(nums)
        return max(len(list(group)) for key, group in groupby(nums) if key == maxval)
