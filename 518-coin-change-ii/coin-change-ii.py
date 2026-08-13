class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        # dp[i][a] = ways using coins[i:] to make amount a
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[n][0] = 1   # with no coins, only amount 0 is possible

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                # skip current coin
                dp[i][a] = dp[i + 1][a]
                # take current coin (if we can)
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]