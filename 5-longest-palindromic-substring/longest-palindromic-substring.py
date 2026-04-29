class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx=0
        rlen=0
        n=len(s)

        for i in range(n):

            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                if rlen<r-l+1:
                    rlen=r-l+1
                    idx=l
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if rlen<r-l+1:
                    rlen=r-l+1
                    idx=l
                l-=1
                r+=1
        return s[idx:idx+rlen]