class Solution:
    def isVowelWord(self, word: str) -> bool: #why need self? 
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        return word[0].lower() in vowels and word[-1].lower() in vowels
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix_sum = [0] * (n + 1)  # Using n+1 to handle 0-based indexing easily
        
        # Build prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if self.isVowelWord(words[i]) else 0)
        
        # Process queries using prefix sum
        result = []
        for left, right in queries:
            # Calculate count of vowel words in range [left, right]
            count = prefix_sum[right + 1] - prefix_sum[left]
            result.append(count)
            
        return result

            

        