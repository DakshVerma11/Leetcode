class Solution:
    def reverse(self, x: int) -> int:
        neg = x<0
        dig=[]
        if neg:
            x*=-1
        while x:
            dig.append(x%10)
            x//=10

        
        res=0
        for digit in dig:
            res*=10
            res+=digit

        if res>2**31:
            return 0
        if neg:
            return -1*res
        return res


