class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        # Try each index as the starting position
        for curr in range(n):
            if nums[curr] == 0:
                # Try moving to the right first
                direction = 1  # Moving right
                temp_nums = nums[:]
                valid = True
                pos = curr
                
                # Simulate the process moving right
                while 0 <= pos < n:
                    if temp_nums[pos] == 0:
                        pos += direction
                    elif temp_nums[pos] > 0:
                        temp_nums[pos] -= 1
                        direction *= -1  # Reverse direction
                        pos += direction
                    else:
                        break  # Out of bounds or invalid situation
                # If the entire list was reduced to zero, it's valid for this starting point
                if all(x == 0 for x in temp_nums):
                    count += 1

                # Now try moving left from the same position
                direction = -1  # Moving left
                temp_nums = nums[:]
                valid = True
                pos = curr
                
                # Simulate the process moving left
                while 0 <= pos < n:
                    if temp_nums[pos] == 0:
                        pos += direction
                    elif temp_nums[pos] > 0:
                        temp_nums[pos] -= 1
                        direction *= -1  # Reverse direction
                        pos += direction
                    else:
                        break  # Out of bounds or invalid situation
                # If the entire list was reduced to zero, it's valid for this starting point
                if all(x == 0 for x in temp_nums):
                    count += 1
        
        return count