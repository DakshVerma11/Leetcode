class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen=0
        
        for j in range(len(s)):
            setchar=set()
            count=0
            i=j
            while i<len(s) and s[i] not in setchar:
                setchar.add(s[i])
                count+=1
                i+=1
            maxlen=max(count,maxlen)
        return maxlen


#Sliding Window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

