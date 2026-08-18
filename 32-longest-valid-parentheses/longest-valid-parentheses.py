class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0

        # Left -> Right
        left = 0
        right = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                res = max(res, 2 * right)
            elif right > left:
                left = right = 0

        # Right -> Left
        left = 0
        right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0

        return res

                    
                