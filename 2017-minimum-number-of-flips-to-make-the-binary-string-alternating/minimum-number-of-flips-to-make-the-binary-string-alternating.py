class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s_double = s + s
        
        # Build target alternating strings of length 2*n
        alt1 = "".join("0" if i % 2 == 0 else "1" for i in range(2 * n))
        alt2 = "".join("1" if i % 2 == 0 else "0" for i in range(2 * n))
        
        diff1, diff2 = 0, 0
        ans = float('inf')
        left = 0
        
        for right in range(2 * n):
            # Track mismatches with target patterns
            if s_double[right] != alt1[right]:
                diff1 += 1
            if s_double[right] != alt2[right]:
                diff2 += 1
                
            # Maintain a window of length n
            if right - left + 1 > n:
                if s_double[left] != alt1[left]:
                    diff1 -= 1
                if s_double[left] != alt2[left]:
                    diff2 -= 1
                left += 1
                
            # Update minimum flips when window size reaches n
            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)
                
        return ans