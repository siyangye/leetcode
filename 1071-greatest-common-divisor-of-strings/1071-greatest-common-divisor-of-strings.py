class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = ""
        min_prefix = ""
        for char in str1:
            prefix += char
            if len(str1)%len(prefix)== 0 and len(str2)%len(prefix) == 0:
                count1 = len(str1)//len(prefix)
                count2 = len(str2)//len(prefix)
                if str1 == count1 * prefix and str2 == count2 * prefix:
                    min_prefix = prefix
                # else:
        return min_prefix

