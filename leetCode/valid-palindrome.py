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

    #정규식 이용
    def isPalindrome2(self, s: str) -> bool:
        lower_s = s.lower()
        lower_s = re.sub('[^a-z0-9]','',lower_s)
        return lower_s==lower_s[::-1]


Solution.isPalindrome2(Solution,"A man, a plan, a canal: Panama")