class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        powers = []
        for i in range(32):
            if (n >> i) & 1:
                powers.append(1 << i)
        
        for i in range(1, len(powers)):
            powers[i] = (powers[i] * powers[i - 1]) % MOD
        
        res = []
        for left, right in queries:
            curr = powers[right]
            if left > 0:
                curr = (curr * pow(powers[left - 1], MOD - 2, MOD)) % MOD
            res.append(curr)
        
        return res