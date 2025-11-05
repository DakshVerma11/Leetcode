class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n==1:
            return 2
    
        lsum = [0]*n 
        rsum = [0]*n
        for i in range(1,n):
            lsum[i] = lsum[i-1]+nums[i-1]
        for i in range(n-2,-1,-1): #missed rsum[0]
            rsum[i] = rsum[i+1]+nums[i+1]
        # print(lsum)
        # print(rsum)
        # print("-----------")
        for i in range(n):
            if nums[i] != 0:
                continue
            if lsum[i] == rsum[i]:
                res+=2
            if abs(lsum[i]-rsum[i]) == 1:
                res+=1
        return res