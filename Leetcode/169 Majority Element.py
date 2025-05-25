class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[int(len(nums)/2)]




class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=defaultdict(int)
        maxcount,res=0,0
        for n in nums:
            count[n]=1+count.get(n,0)
            if count[n] > maxcount:
                maxcount=count[n]
                res = n
        return res






#Boyer Moore Algo

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res
