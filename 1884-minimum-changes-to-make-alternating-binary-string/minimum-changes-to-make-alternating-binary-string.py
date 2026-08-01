class Solution:
    def minOperations(self, s: str) -> int:
        count_pattern1 = 0  # Operations needed for "010101..."
        
        for i, char in enumerate(s):
            # For "010101...", even indices should be '0' and odd should be '1'
            expected = '0' if i % 2 == 0 else '1'
            if char != expected:
                count_pattern1 += 1
                
        n = len(s)
        # The number of changes for "101010..." is simply (n - count_pattern1)
        return min(count_pattern1, n - count_pattern1)