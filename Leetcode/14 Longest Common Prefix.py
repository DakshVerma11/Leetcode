class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
    
        strs.sort()
        length = min(len(strs[0]), len(strs[-1]))
        j=0
        for i in range(length):
            if strs[0][i]!=strs[-1][i]:
                break
            j+=1

        return strs[0][0:j]
