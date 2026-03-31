# Last updated: 3/31/2026, 7:09:39 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums)-1
5
6        while left <= right:
7
8            mid = left + (right-left)//2 
9
10            if nums[mid] == target:
11                return mid 
12            elif nums[mid] > target:
13                right = mid - 1
14            else:
15                left = mid + 1 
16        return -1 