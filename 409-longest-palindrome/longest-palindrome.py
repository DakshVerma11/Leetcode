class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        res=-1
        for frequency in freq.values():
            if frequency%2==1:
                res+=1
        return len(s)-res if res>=0 else len(s)