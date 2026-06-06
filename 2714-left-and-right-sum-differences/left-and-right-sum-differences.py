class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightsum=sum(nums)
        n=len(nums)
        leftsum=0
        res=[0]*n
        for i in range(n):
            leftsum+=nums[i]
            res[i]=abs(rightsum-leftsum)
            rightsum-=nums[i]
        return res