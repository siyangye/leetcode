class Solution:
    def isPalindrome(self, s: str) -> bool:
        def updateStr(s:str) ->str:
            res = ""
            i = 0
            while i < len(s):
                if s[i].isalnum():
                    res += s[i].lower()  # Fixed: added = for concatenation
                i += 1
            return res
        
        letterOnlyStr = updateStr(s)
        print(letterOnlyStr)   # Now this will work
        m, n = 0, len(letterOnlyStr)-1
        while m < n:
            if letterOnlyStr[m] != letterOnlyStr[n]:
                return False
            m += 1
            n -= 1
        return True