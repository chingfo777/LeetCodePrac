class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for placing the valid elements (not equal to val)
        k = 0
        
        # Iterate through all elements in the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k