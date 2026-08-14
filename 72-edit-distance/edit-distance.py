class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp={}
        def dfs(idx1,idx2):
            if idx2==m:
                return n-idx1
            if idx1==n:
                return m-idx2
            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]
            
            if word1[idx1]==word2[idx2]:
                dp[(idx1,idx2)]=dfs(idx1+1,idx2+1)
                return dp[(idx1,idx2)]
            dp[(idx1,idx2)]=1+min(dfs(idx1+1,idx2),dfs(idx1,idx2+1),dfs(idx1+1,idx2+1))
            return dp[(idx1,idx2)]            
            


        return dfs(0,0)