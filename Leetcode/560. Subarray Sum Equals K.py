class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumlist=[0]*(len(nums)+1)
        for i in range(1, len(nums) + 1):
            sumlist[i] = sumlist[i - 1] + nums[i - 1]

        count=0
        for i in range(len(sumlist)):
            for j in range(i+1,len(sumlist)):
                if sumlist[j]-sumlist[i]==k:
                    count+=1
        return count



class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumdict={0:1}
        count=0
        curSum=0

        for n in nums:
            curSum+=n
            count+=sumdict.get(curSum-k,0)
            sumdict[curSum]=1+sumdict.get(curSum,0)
        return count







