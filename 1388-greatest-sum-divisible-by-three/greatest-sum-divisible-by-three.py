class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        lastSum = [0, float('-inf'), float('-inf')]

        for num in nums:
            prev = lastSum[:]

            for i in range(3):
                rem = (i + num) % 3
                lastSum[rem] = max(lastSum[rem], prev[i] + num)

        return lastSum[0]