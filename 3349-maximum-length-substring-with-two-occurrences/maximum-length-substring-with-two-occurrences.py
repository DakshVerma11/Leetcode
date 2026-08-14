class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans=0
        l=0
        freq=defaultdict(int)
        for r in range(len(s)):
            freq[s[r]]+=1
            if freq[s[r]]==3:
                while s[l]!=s[r]:
                    freq[s[l]]-=1
                    l+=1
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans