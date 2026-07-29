class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Ignore leading whitespace
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        # 2. Determine sign
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        result = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # 3. Read valid digits
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1
            
        result *= sign
        
        # 4. Clamp within 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result