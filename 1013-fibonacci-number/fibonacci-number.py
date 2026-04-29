class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        i0=0
        i1=1
        for i in range(n-1):
            i0,i1=i1,i0+i1
        return i1