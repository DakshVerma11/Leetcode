class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3==0:
                n//=3
            elif n%3==1:
                n-=1
                n//=3
            else:
                return False
        return True