class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        res = 0


        l=0
        maxf=0
        for r in range(len(s)):
            count[s[r]]+=1
            if maxf<count[s[r]]:
                maxf=count[s[r]]
            while (r-l+1)-maxf >k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
