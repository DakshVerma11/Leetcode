class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_maximums = self.sum_of_subarray_maximums(nums, n)
        sum_of_minimums = self.sum_of_subarray_minimums(nums, n)
        return sum_of_maximums - sum_of_minimums

    def sum_of_subarray_minimums(self, nums, n):
        total = 0
        stack = []  # stores indices, maintains increasing order of values

        for i in range(n + 1):
            # Sentinel to flush remaining elements at the end
            current_val = float('-inf') if i == n else nums[i]

            while stack and nums[stack[-1]] >= current_val:
                mid = stack.pop()
                left_boundary = stack[-1] if stack else -1
                right_boundary = i

                left_count = mid - left_boundary
                right_count = right_boundary - mid
                total += nums[mid] * left_count * right_count

            if i < n:
                stack.append(i)

        return total

    def sum_of_subarray_maximums(self, nums, n):
        total = 0
        stack = []  # stores indices, maintains decreasing order of values

        for i in range(n + 1):
            # Sentinel to flush remaining elements at the end
            current_val = float('inf') if i == n else nums[i]

            while stack and nums[stack[-1]] <= current_val:
                mid = stack.pop()
                left_boundary = stack[-1] if stack else -1
                right_boundary = i

                left_count = mid - left_boundary
                right_count = right_boundary - mid
                total += nums[mid] * left_count * right_count

            if i < n:
                stack.append(i)

        return total