class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list=list(a[::-1])
        b_list=list(b[::-1])

        carry=0

        length=max(len(a_list), len(b_list))
        c=[]

        for i in range(length):
            val_a = int(a_list[i]) if i < len(a_list) else 0
            val_b = int(b_list[i]) if i < len(b_list) else 0
            
            total = val_a + val_b + carry
            c.append(str(total % 2))
            carry = total // 2
            
        if carry:
            c.append("1")
            
        return "".join(c[::-1])