from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character
        freq = Counter(word)
        
        # Sort frequencies in descending order
        sorted_counts = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        for i, count in enumerate(sorted_counts):
            # Calculate multiplier based on index (0-7 -> 1, 8-15 -> 2, etc.)
            pushes_per_char = (i // 8) + 1
            total_pushes += count * pushes_per_char
            
        return total_pushes