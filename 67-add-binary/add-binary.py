class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        # Process digits from right to left as long as there are digits or a carry left
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # The current binary digit is total % 2
            result.append(str(total % 2))
            # The new carry is total // 2
            carry = total // 2

        # Since we appended least significant digits first, reverse the result
        return "".join(reversed(result))