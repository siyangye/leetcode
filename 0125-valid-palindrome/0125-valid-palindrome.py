class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        print(string)
        l=0
        r=len(s)-1
        while l<r:
            if not string[l].isalnum():
                l+=1
                continue
            if not string[r].isalnum():
                r-=1
                continue
            if string[l]==string[r]:
                l+=1
                r-=1
            else:
                # print(string[l])
                # print(string[r])
                return False
        return True