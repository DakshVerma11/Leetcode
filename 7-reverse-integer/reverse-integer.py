class Solution:
    def reverse(self, x: int) -> int:
        neg = x<0
        dig=[]
        if neg:
            x*=-1
        while x:
            dig.append(x%10)
            x//=10
        dig.reverse()
        ans=0
        base=1
        for i in dig:
            ans+=i*base
            base*=10
        if ans>2**31:
            return 0
        if neg:
            ans*=-1
        return ans