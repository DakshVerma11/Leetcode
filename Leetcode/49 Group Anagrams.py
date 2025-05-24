class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
    
        countS={}
        countT={}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
    
        return True
    
    
      
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)<2:
            return [strs]
            
        ans=[]
        
        while strs:
            cur=[strs[0]]
            i = 1
            while i < len(strs):
                if not self.isAnagram(strs[0],strs[i]):
                    i+=1
                    continue
                cur.append(strs[i])
                del strs[i]
            ans.append(cur)
            del strs[0]
        return ans
