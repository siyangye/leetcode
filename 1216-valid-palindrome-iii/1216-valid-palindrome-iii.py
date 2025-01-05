class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def helper(left: int, right: int, k: int) -> bool:
            # 基本情况
            if k < 0:  # 删除次数用完
                return False
            if left >= right:  # 检查完所有字符
                return True
                
            # 如果字符相同，继续检查内部字符
            if s[left] == s[right]:
                return helper(left + 1, right - 1, k)
            
            # 字符不同，尝试删除左边或右边的字符
            return helper(left + 1, right, k - 1) or \
                   helper(left, right - 1, k - 1)
        
        return helper(0, len(s) - 1, k)
        # @cache  # 添加记忆化
        # def minDeletions(left: int, right: int) -> int:
        #     if left >= right:
        #         return 0
                
        #     if s[left] == s[right]:
        #         return minDeletions(left + 1, right - 1)
            
        #     return 1 + min(minDeletions(left + 1, right), 
        #                  minDeletions(left, right - 1))
        
        # return minDeletions(0, len(s) - 1) <= k