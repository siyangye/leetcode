class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def moves(l,r)-> int:
            if l >= r:
                return 0
            elif s[l]==s[r]:
                return moves(l+1,r-1)
            else:
                return 1+ min(moves(l+1,r),moves(l,r-1))
        return moves(0,len(s)-1)<=k

        