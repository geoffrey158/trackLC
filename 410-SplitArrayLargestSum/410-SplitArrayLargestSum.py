# Last updated: 11/2/2025, 8:22:34 PM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # Helper function to check if we can split the array into
        # at most k subarrays where each subarray sum is <= maxSum
        def canSplit(maxSum):
            subarray = 1  # Start with one subarray
            curr_sum = 0  # Current subarray sum

            for num in nums:
                # If adding this number exceeds the allowed maxSum
                curr_sum += num
                if curr_sum > maxSum:
                    subarray += 1   # We need a new subarray
                    if subarray > k:
                        # Too many subarrays needed — can't split under this `largest`
                        return False
                    curr_sum = num #Start a new subarray with current num
            
            # Valid Split using <= k subarrays
            return True 

        # Binary search bounds:
        # Minimum possible largest subarray sum is the max element (cannot split a single number)
        # Maximum possible is the total sum (no splits)
        left = max(nums) 
        right = sum(nums)
        res = right #return value, store the minimum valid largest sum
        # Binary search to find the smallest max subarray sum that allows a valid split
        while left <= right:
            mid = left + (right - left) // 2  # Try middle value as potential max subarray sum
            
            if canSplit(mid):
                # If we can split with current mid as maxSum,
                # try to find a smaller valid maximum
                res = mid #update return value 
                right = mid - 1 
            else:
                # If we can't split properly, need to allow a larger maxSum
                left = mid + 1

        return res

        #Time: O(n * log(sum(nums)-max(nums))), For each binary search step, we do an O(n) scan.
        #Space: O(1) (constant extra space)