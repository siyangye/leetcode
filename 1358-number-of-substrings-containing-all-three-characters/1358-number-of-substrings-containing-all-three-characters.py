class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            
            # Shrink the window from the left as much as possible
            # while still containing all three characters
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                char_count[s[left]] -= 1
                left += 1
            
            # Count valid substrings ending at right
            # Any position from 0 to (left-1) can be a valid start
            count += left
            
        return count