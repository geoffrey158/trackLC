# Last updated: 11/2/2025, 8:22:22 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #list is sorted in asecnding order, so we can use binary search
        left = 0 
        right = len(nums) - 1 

        #edge case: <=, if array only has one element we still want to check if the target exists 
        while left <= right:
            mid = left + (right-left)//2 

            if nums[mid] == target:
                return mid #return idx of where the target is 
            elif nums[mid] > target: #that means the target cannot be at mid or the right 
                right = mid - 1 
            else: #target cannot be at mid or the left
                left = mid + 1 
        
        return -1 #target does not exist in the list 

        #Time complexity: O(logn)
        #Space complexity: O(1)