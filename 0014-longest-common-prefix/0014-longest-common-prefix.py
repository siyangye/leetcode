class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        list = []
        for c in strs[0]:
            list.append(c)
        for i in range(len(strs)):
            for j in range(len(list)):
                if j >= len(strs[i]):
                    list = list[:j]
                else:
                    if strs[i][j]!=strs[0][j]:
                       list = list[:j]
                
        return "".join(list)