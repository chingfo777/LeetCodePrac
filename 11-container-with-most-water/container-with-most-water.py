class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate current area
            current_height = min(height[left], height[right])
            current_width = right - left
            current_water = current_height * current_width
            
            # Update maximum area
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water