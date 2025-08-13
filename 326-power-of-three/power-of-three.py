class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if  n<1:
            return False
        while n>1:
            #print(n)
            if n%3!=0:
                return False
            n//=3
        #print("Final ",n)
        return True if n else False