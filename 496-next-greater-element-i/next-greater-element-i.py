class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterElementIndex={}
        stack=[]

        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                nextGreaterElementIndex[nums2[i]]=-1
            else:
                nextGreaterElementIndex[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        #print(nextGreaterElementIndex)
        res=[]
        for i in nums1:
            res.append(nextGreaterElementIndex[i])
        return res