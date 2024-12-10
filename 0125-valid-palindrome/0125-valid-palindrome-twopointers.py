class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_s = ""
        for i in s:
            if i.isalnum():
                updated_s+=i
    
        if updated_s.lower()==updated_s[::-1].lower():
            return True
        else:
            return False