# Last updated: 11/2/2025, 8:23:43 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search since the array was originally sorted 
        left = 0 
        right = len(nums) - 1 

        while left < right:
        #important to check if the array has been rotated 
            mid = left + (right-left)//2 

            #that means the pivot is to the right, min has to be on the right side 
            if nums[mid] > nums[right]: 
                left = mid+1 
            else: #pivot is to the left or there is no pivot, min has to be on the left side
                right = mid #don't do mid-1 bc mid could still be the min element of the array
                #edge case: the pivot could still be at mid

        return nums[left]#return the min element(not the idx), could return left or right since we converged the values of left and right 
        
        #Time Complexity:O(logn)
        #Space Complexity:O(1)