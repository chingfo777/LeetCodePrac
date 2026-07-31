class Solution:
    def minOperations(self, s: str) -> int:
        count_pattern1 = 0  # Operations needed to match "010101..."
        
        for i, char in enumerate(s):
            # Expected character for pattern starting with '0'
            expected = '0' if i % 2 == 0 else '1'
            if char != expected:
                count_pattern1 += 1
                
        # Total length of the string
        n = len(s)
        
        # Minimum between changing to "010101..." and "101010..."
        return min(count_pattern1, n - count_pattern1)