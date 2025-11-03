# Last updated: 11/2/2025, 8:23:37 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        mid = (left + right)//2
        return nums[mid]