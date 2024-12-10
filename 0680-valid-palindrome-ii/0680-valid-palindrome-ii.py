class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPanlindrome(s:str,l:int, r:int)-> bool:
            while l <r:
                if s[l] ==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

        if s == s[::-1]:
            return True
        else:
            l,r = 0, len(s)-1
            while l <r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else: return (checkPanlindrome(s,l+1,r))or (checkPanlindrome(s,l,r-1))
    
        