# Last updated: 11/2/2025, 8:23:31 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 #left pointer of sliding window 
        total = 0 #keeps track of the sum of the sliding window 
        res = float('inf') #return value, store the minimum length found 

        #move right pointer through array 
        for right in range(len(nums)):
            total += nums[right] #slide the window by adding the current number on the right window 

            #if total is greater than or equal to target 
            #shrink window from the left until total < target 
            while total >= target:
                res = min(right-left+1,res) #update minimum length if the window is smaller 
                total -= nums[left] #shrink the window from the left 
                left += 1
        
        #If res was from original float('inf') value, return it; otherwise, no valid subarray found
        return 0 if res == float("inf") else res

        #Time complexity: O(n), the list gets traversed once 
        #Space complexity: O(1), no extra space is used 

