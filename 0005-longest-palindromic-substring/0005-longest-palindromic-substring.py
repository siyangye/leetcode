def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    start = 0  # 最长回文子串的起始位置
    max_length = 1  # 最长回文子串的长度，初始为1（单个字符）
    
    # 辅助函数：从中心向两边扩展
    def expand_around_center(left, right):
        # 当指针在有效范围内且左右字符相等时，继续扩展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回有效回文串的起始和结束位置
        return left + 1, right - 1
    
    # 遍历字符串中的每个位置
    for i in range(len(s)):
        # 情况1：以单个字符为中心（奇数长度回文串）
        left1, right1 = expand_around_center(i, i)
        length1 = right1 - left1 + 1
        
        # 情况2：以两个字符之间为中心（偶数长度回文串）
        left2, right2 = expand_around_center(i, i + 1)
        length2 = right2 - left2 + 1
        
        # 更新最长回文串记录
        if length1 > max_length:
            max_length = length1
            start = left1
        
        if length2 > max_length:
            max_length = length2
            start = left2
    
    # 返回最长回文子串
    return s[start:start + max_length]