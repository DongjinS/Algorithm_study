class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = []
        for c in s:
            if c.isalpha():
                lower_s.append(c.lower())
            elif c.isdigit():
                lower_s.append(c)
                
        if lower_s==list(reversed(lower_s)):return True
        else:return False        