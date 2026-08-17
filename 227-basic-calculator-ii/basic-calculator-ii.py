class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        prev_op = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                current_num = current_num * 10 + int(c)

            # Process when we hit an operator or the end of string
            if c in "+-*/" or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(current_num)
                elif prev_op == '-':
                    stack.append(-current_num)
                elif prev_op == '*':
                    stack.append(stack.pop() * current_num)
                elif prev_op == '/':
                    # Truncate toward zero (Python's // rounds toward -inf)
                    stack.append(int(stack.pop() / current_num))
                prev_op = c
                current_num = 0

        return sum(stack)

