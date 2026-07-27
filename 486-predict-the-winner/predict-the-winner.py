class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] the max relative score diff for subarray nums[i...j]
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = nums[i]
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Maximize current pick minus the opponent's subsequent score
                pick_left = nums[i] - dp[i + 1][j]
                pick_right = nums[j] - dp[i][j - 1]
                
                dp[i][j] = max(pick_left, pick_right)
                
        return dp[0][n - 1] >= 0