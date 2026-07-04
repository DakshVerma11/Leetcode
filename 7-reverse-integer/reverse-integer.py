class Solution:
    def reverse(self, x: int) -> int:
        neg = x<0
        dig=[]
        if neg:
            x*=-1
        res=0
        while x:
            res*=10
            res+=x%10
            x//=10
            

        if res>2**31:
            return 0
        if neg:
            return -1*res
        return res


