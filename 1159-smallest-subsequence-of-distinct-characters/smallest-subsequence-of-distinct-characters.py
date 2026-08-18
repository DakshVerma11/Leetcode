class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndex={j:i for i,j in enumerate(s)}
        #print(lastIndex)

        res=[]
        seen=set()
        for i in range(len(s)):
            if s[i] not in seen:
                while res and res[-1]>s[i] and i<lastIndex[res[-1]]:
                    
                    seen.remove(res.pop())
                res.append(s[i])
                seen.add(s[i])
        return ''.join(res)