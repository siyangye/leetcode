class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for c in s:
            if c.isalnum():
                string.append(c.lower())
        print(string)
        return string == string[::-1] #reverse list 