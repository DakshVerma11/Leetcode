class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length = min(len(word1),len(word2))
        i=0
        res=[]
        while i<length:
            res.append(word1[i])
            res.append(word2[i])
            i+=1
        if length<len(word1):
            res.append(word1[length::])
        elif length<len(word2):
            res.append(word2[length::])

        return ''.join(res)
