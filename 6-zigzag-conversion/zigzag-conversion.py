class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or greater than/equal to the string length
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Array of strings to represent each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the characters and place them in the correct row
        for char in s:
            rows[current_row] += char
            
            # Change direction when reaching top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down based on current direction
            current_row += 1 if going_down else -1
            
        # Join all row strings together
        return ''.join(rows)