class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        updated_s=sorted(s)
        updated_t = sorted(t)
        for i in range(len(s)):
            if updated_s[i]!=updated_t[i]:
                return False
        return True

        