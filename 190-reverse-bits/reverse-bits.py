class Solution:
    def reverseBits(self, n: int) -> int:
        ans=[0]*32
        i=0
        while n:
            ans[i]=n%2
            n//=2
            i+=1
        
        res = 0
        for bit in ans:
            res = (res << 1) | int(bit)
        return res