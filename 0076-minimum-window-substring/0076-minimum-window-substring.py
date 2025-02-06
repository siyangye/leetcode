class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create frequency map for string t
        need = Counter(t)
        
        # Initialize variables
        missing = len(t)  # Count of characters we still need
        start = 0  # Start of current window
        min_start = 0  # Start of minimum window
        min_len = float('inf')  # Length of minimum window
        
        # Iterate through string s using sliding window
        for end, char in enumerate(s):
            # If current character is needed
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            # When we have all characters
            if missing == 0:
                # Remove unnecessary characters from start
                while need[s[start]] < 0:
                    need[s[start]] += 1
                    start += 1
                
                # Update minimum window if current window is smaller
                if end - start + 1 < min_len:
                    min_start = start
                    min_len = end - start + 1
                
                # Move start pointer and continue searching
                need[s[start]] += 1
                missing += 1
                start += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""