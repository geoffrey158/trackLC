# Last updated: 11/2/2025, 8:23:38 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1-index array, return indexes also as 1-indexed 
        #two pointer approach 
        left = 0
        right = len(numbers) - 1 

        while left <= right:
            
            currSum = numbers[left] + numbers[right]

            if currSum == target: 
                return [left+1,right+1] #return +1 bc we want 1-indexed result 
            elif currSum < target:#sum is less than target, move the left pointer to the right to increase the sum
                left += 1 
            else:#sum is greater than target, move the right pointer to the left to decrease the sum
                right -= 1 
        
        #Time complexity: O(n), Input array travesed at most once
        #Space complexity: O(1), We only use additional space to store two indices and the sum
            
            