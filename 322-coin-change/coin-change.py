class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for curAmount in range(1,amount+1):
            for coinVal in coins:
                if curAmount-coinVal>=0:
                    dp[curAmount]=min(dp[curAmount],1+dp[curAmount-coinVal])
        return dp[amount] if dp[amount] != float('inf') else -1