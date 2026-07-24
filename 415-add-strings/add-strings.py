class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            # Convert single character digit to integer using ASCII value
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Compute sum of digits and carry
            total = d1 + d2 + carry
            carry = total // 10
            result.append(str(total % 10))
            
            i -= 1
            j -= 1
            
        # Reverse list and join to form the final result string
        return "".join(reversed(result))