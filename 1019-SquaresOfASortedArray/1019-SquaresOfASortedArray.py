# Last updated: 11/2/2025, 8:22:14 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        length = len(nums) 
        #Two points left and right 
        left = 0 
        right = length - 1
        result = [0] * length #Need to set output list size to the size of the nums list
        
        #Iterate backwards b/c no guarantee large elments are at the ends of the array
        #Ensures that the squares of the larger elements occupy the higher indices of the result array 
        for i in range(length - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right] * nums[right]
                right -= 1 
            else:
                result[i] = nums[left] * nums[left]
                left += 1
        
        return result 

        #Time Complexity: O(N), where N is the lenght of nums 
        #Space Complexity: O(N), if you take output into account and O(1) otherwise 
        