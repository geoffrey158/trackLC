# Last updated: 11/2/2025, 8:23:15 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = True 
        zerocount = 0
        slide = 0
        for i in range (len(nums)):       
            if nums[i] != 0:
                nums[slide] = nums[i]
                slide += 1 
            else:
                zerocount += 1 
        
        while zerocount > 0:
            nums[len(nums)-zerocount] = 0
            zerocount -= 1
        


