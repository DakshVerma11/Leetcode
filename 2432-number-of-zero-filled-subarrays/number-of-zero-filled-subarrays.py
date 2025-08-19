class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        consecutiveZeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                consecutiveZeros+=1
            else:
                ans+=((consecutiveZeros)*(consecutiveZeros+1))//2
                consecutiveZeros=0
        ans+=((consecutiveZeros)*(consecutiveZeros+1))//2
        return ans
