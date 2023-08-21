class Solution:
    def firstUniqChar(self, s: str) -> int:
        #use hashMap to count the occurances of each char
        
        #find the char with char_value = 1 (if loop break),
        #get the index with: enumerate()
        
        char_count = {} #char:char_count
        for char in s:
            if char in char_count:
                char_count[char] += 1  #dict[key] => value 
            else:
                char_count[char] = 1 
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index 
        #out of loop:
        return -1