"""first confirm, the input string only have letters? 
do we need to handle empty string? 
output is int.
letters even - we could use all
letters are odd - we could use 1 of it. 
2,1
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        useMiddle = False
        chars = {}
        res = 0
        for letter in s:
            chars[letter] = chars.get(letter, 0) + 1 
        for char, count in chars.items(): #count: 1,2,...
            if count % 2 == 0:
                res += count
            else:
                res += count - 1 #count: 1,3,5,7 -> 0,2,4,6
                if not useMiddle:
                    res += 1
                    useMiddle = True
        return res



        