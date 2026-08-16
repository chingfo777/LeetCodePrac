class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                # Pop the top element if stack is non-empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the current closing bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were properly closed
        return len(stack) == 0