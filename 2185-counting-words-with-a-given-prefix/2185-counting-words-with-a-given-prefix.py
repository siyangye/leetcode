class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count =0
        n=len(pref)
        for word in words:
            if len(word)>=len(pref)and pref==word[:n]:
                count+=1
        return count
        