class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        #sliding window pointer
        l = 0 
        res = 0
        
        for r in range(len(s)):
            #出现重复数字:
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            #没有出现重复, 则续增加数字：
            charSet.add(s[r])
            charLen = r - l + 1 # 左右两端指针位置相减，得到substring的长度
            res = max(res, charLen)
        
        return res
                
                
                
            