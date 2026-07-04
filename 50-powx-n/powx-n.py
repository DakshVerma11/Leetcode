class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_power(base: float, exponent: int) -> float:
            result = 1.0
            while exponent:
                if exponent & 1:
                    result *= base
                base *= base
                exponent >>= 1
            return result

        return quick_power(x, n) if n >= 0 else 1 / quick_power(x, -n)