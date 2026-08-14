class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5=0
        bill10=0

        for bill in bills:
            if bill==5:
                bill5+=1
            if bill==10:
                if bill5>0:
                    bill5-=1
                    bill10+=1
                else:
                    return False
            if bill==20:
                if bill10>0 and bill5>0:
                    bill10-=1
                    bill5-=1
                elif bill5>2:
                    bill5-=3
                else:
                    return False
        return True