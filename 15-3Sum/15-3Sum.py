# Last updated: 8/28/2026, 2:20:41 AM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        res = []
4        nums.sort()
5
6        for i in range(len(nums)-1):
7            #if the first element is greater than 0 
8            if nums[i] > 0:
9                break
10
11            if i > 0 and nums[i] == nums[i-1]:
12                continue 
13
14            a = nums[i]
15            left = i + 1
16            right = len(nums)-1
17
18            while left < right:
19
20                totalSum = a + nums[left] + nums[right]
21                if totalSum == 0:
22                    res.append([a,nums[left],nums[right]])
23                    left += 1
24                    right -= 1
25                    # Skip duplicate values for the second number
26                    while nums[left] == nums[left - 1] and left < right: #
27                        left += 1
28                    # Skip duplicate values for the third number
29                    while nums[right] == nums[right + 1] and left < right:
30                        right -= 1
31                elif totalSum > 0:
32                    right -= 1
33                else:
34                    left += 1
35            
36        return res 