class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        powerof2=0
        for i in range(1, n+1):
            if (i & (i - 1)) == 0:
                powerof2=i
            ans[i]=1+ans[i-powerof2]
        return ans