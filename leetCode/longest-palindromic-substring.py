class Solution:
    def longestPalindrome(self, s: str) -> str:
        def chknumPalindrome(left: int, right: int) -> int:
            while 0<=left and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        if len(s)<2 or s==s[::-1]:
            return s
        res = ''
        for i in range(len(s)):
            res = max(res, chknumPalindrome(i,i+1),chknumPalindrome(i,i+2), key=lambda x:len(x))
        
        return res
        