
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        last = [0] * 32  # Store the last seen index of each bit (0-31)
        
        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last[bit] = i
            max_len = 1
            for bit in range(32):
                if last[bit]:
                    max_len = max(max_len, last[bit] - i + 1)
            ans[i] = max_len
        return ans
