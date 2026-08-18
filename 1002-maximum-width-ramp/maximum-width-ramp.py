class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack=[0]
        ans=0
        for i in range(1,len(nums)):
            if nums[stack[-1]]>nums[i]:
                stack.append(i)


        for j in range(len(nums)-1,-1,-1):
            while stack and nums[j]>=nums[stack[-1]]:
                ans=max(ans,j-stack[-1])
                stack.pop()
        return ans
