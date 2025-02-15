class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_char = {}
        for c in magazine:
            magazine_char[c] = magazine_char.get(c,0) +1
        for char in ransomNote:
            if char not in magazine_char or magazine_char[char] <= 0:
                return False
            else: #magazine has the char
                magazine_char[char] -= 1
        return True

        