class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr=set(arr)
        ans=0
        while k:
            ans+=1
            while ans in arr:
                ans+=1
            k-=1
        return ans