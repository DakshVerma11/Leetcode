class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count={}

        for i in nums:
            count[i]=count.get(i,0)+1
        res=[]
        for p,q in count.items():
            if q>len(nums)/3:
                res.append(p)

        return res
