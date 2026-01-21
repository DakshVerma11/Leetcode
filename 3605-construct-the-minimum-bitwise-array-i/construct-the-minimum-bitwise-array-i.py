class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        ans=[-1]*len(nums)
        for i in range(len(nums)):
            num=nums[i]
            if num!=2:
                for j in range(1,num):
                    if j|(j+1)==num:
                        ans[i]=j
                        break

        return ans