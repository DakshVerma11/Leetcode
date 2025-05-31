class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<target:
            return 0
        minarr=len(nums)
        l=0
        r=0
        
        while r<=len(nums):
            sums=0
            for i in range(l,r):
                sums+=nums[i]
            
            if sums>=target:
                minarr=min(minarr,r-l)
                l+=1
            else:
                r+=1

        return minarr







class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<target:
            return 0
        
        l, total = 0, 0
        res = len(nums)

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return res
