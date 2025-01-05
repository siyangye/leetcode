class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache  # 添加记忆化
        def minDeletions(left: int, right: int) -> int:
            if left >= right:
                return 0
                
            if s[left] == s[right]:
                return minDeletions(left + 1, right - 1)
            
            return 1 + min(minDeletions(left + 1, right), 
                         minDeletions(left, right - 1))
        
        return minDeletions(0, len(s) - 1) <= k