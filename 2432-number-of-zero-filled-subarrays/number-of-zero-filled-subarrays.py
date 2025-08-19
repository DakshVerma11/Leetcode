class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        consecutiveZeros=0
        for i in nums:
            if i==0:
                consecutiveZeros+=1
                ans+=consecutiveZeros

            else:
                consecutiveZeros=0
        return ans
