class Solution:
    def isValid(self, s: str) -> bool:
        # Fast exit: an odd-length string cannot be valid
        if len(s) % 2 != 0:
            return False
        
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                # If stack is non-empty, pop the top; otherwise use a dummy sentinel
                top_element = stack.pop() if stack else '#'
                
                # If opening bracket doesn't match the required one, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening bracket onto the stack
                stack.append(char)
                
        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0