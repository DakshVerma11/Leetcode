class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[-1]*n for _ in range(m)]
        def dfs(idxS,idxT):
            if idxT==n:
                return 1
            if idxS==m:
                return 0
            if dp[idxS][idxT]!=-1:
                return dp[idxS][idxT]
            res=dfs(idxS+1,idxT)
            res+=dfs(idxS+1,idxT+1) if s[idxS]==t[idxT] else 0
            dp[idxS][idxT]=res
            return res
        return dfs(0,0)