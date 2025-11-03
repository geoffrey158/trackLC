# Last updated: 11/2/2025, 8:23:32 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #if there are two distinct indices that are equal to each other and less than k 
        hashset = set()
        left = 0

        for right in range(len(nums)):

            if abs(right - left) > k:
                hashset.remove(nums[left])
                left += 1 
            
            if nums[right] in hashset:
                return True 
            hashset.add(nums[right])
        return False 