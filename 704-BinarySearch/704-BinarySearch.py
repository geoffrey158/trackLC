# Last updated: 1/20/2026, 6:18:37 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        #binary search you start with a left and right poitner and then converage into the middle and search like that 
5        #keep on looping until we find our answer
6
7        left = 0 
8        right = len(nums)-1 
9
10        #<= bc the list could be empty so we use for that
11        while left <= right:
12            mid = left + (right-left)//2 
13
14            if nums[mid] == target:
15                return mid # return index 
16            elif nums[mid] > target:
17                right = mid-1 
18            else:
19                left = mid+1
20            
21        return -1 #if the target is not found
22
23
24            