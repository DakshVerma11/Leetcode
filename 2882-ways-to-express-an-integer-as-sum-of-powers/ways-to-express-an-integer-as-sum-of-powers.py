class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        max_base = 1
        while (max_base + 1) ** x <= n:
            max_base += 1

        dp = [0] * (n + 1)
        dp[0] = 1  # one way to form sum 0: using no numbers

        for i in range(1, max_base + 1):
            power_val = i ** x
            for target in range(n, power_val - 1, -1):
                dp[target] = (dp[target] + dp[target - power_val]) % MOD

        return dp[n]