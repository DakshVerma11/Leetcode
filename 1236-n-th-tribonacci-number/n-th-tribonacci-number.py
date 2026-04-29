class Solution:
    def tribonacci(self, n: int) -> int:
        if n<1:
            return 0
        if n<3:
            return 1
        
        T=[0] * (n + 1)
        T[1]= 1
        T[2] = 1
        for i in range(3,n+1):
            T[i] = T[i-3] + T[i-2] + T[i-1]
        #print(T)
        return T[n]
