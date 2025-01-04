class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def minDeletions(left: int, right: int) -> int:
            # 基本情况
            if left >= right:
                return 0
                
            # 如果字符相同，不需要删除
            if s[left] == s[right]:
                return minDeletions(left + 1, right - 1)
            
            # 字符不同，取删除左边或右边的最小值，加1
            return 1 + min(minDeletions(left + 1, right), 
                         minDeletions(left, right - 1))
        
        # 计算需要的最小删除数，与k比较
        return minDeletions(0, len(s) - 1) <= k