class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        dp[m][n]=1
        def dfs(idxS, idxP):
            if dp[idxS][idxP] != -1:
                return dp[idxS][idxP] == 1

            # Pattern exhausted
            if idxP == n:
                dp[idxS][idxP] = int(idxS == m)
                return idxS == m

            first_match = (
                idxS < m and
                (p[idxP] == '.' or p[idxP] == s[idxS])
            )

            # Next character is '*'
            if idxP + 1 < n and p[idxP + 1] == '*':
                # Case 1: zero occurrences
                # Case 2: consume one character
                ans = (
                    dfs(idxS, idxP + 2) or
                    (first_match and dfs(idxS + 1, idxP))
                )
            else:
                ans = first_match and dfs(idxS + 1, idxP + 1)

            dp[idxS][idxP] = int(ans)
            return ans

        return dfs(0, 0)