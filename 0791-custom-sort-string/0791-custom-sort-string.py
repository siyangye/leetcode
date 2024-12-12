class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict ={}
        for c in order:
            dict[c]=[] #initialize an hashmap, key is letter in order, value is empty list.
        unsorted_s=""
        for l in s:
            
            if l in dict:
                dict[l].append(l)
            else:
                unsorted_s += l
        sorted_s = ""
        for c in order:
            sorted_s += ''.join(dict[c])  # Add all occurrences of each character
            
        return sorted_s + unsorted_s