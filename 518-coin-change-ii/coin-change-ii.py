class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n=len(coins)
        dp=[[-1]*(amount+1) for i in range(n)]
        def dfs(idx: int, remainingAmount: int) -> int:
            if remainingAmount == 0:
                dp[idx][remainingAmount]=1
                return dp[idx][remainingAmount]
            if idx >= n or remainingAmount < coins[idx]:
                return 0
            if dp[idx][remainingAmount]!=-1:
                return dp[idx][remainingAmount]
            dp[idx][remainingAmount] = dfs(idx + 1, remainingAmount)
            dp[idx][remainingAmount] += dfs(idx, remainingAmount - coins[idx])
            return dp[idx][remainingAmount]

        return dfs(0, amount)