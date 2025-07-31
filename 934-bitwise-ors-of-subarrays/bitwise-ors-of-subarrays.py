class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # two sets
        res = set()  
        cur = set() 
        for num in arr:
            new_cur = set()
            # Add OR of each element in `cur` with the new number `num`
            for val in cur:
                new_cur.add(val | num)
            new_cur.add(num)
            cur = new_cur
            for val in cur:
                res.add(val)
        
        return len(res)