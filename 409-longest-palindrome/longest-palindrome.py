class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        oddPalin=False
        res=0
        for frequency in freq.values():
            if frequency%2==1:
                res+=frequency-1
                oddPalin=True
            else:
                res+=frequency
        return res+oddPalin