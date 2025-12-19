# Last updated: 12/19/2025, 6:25:50 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3
4        currSum = 0 #Keep the running count of the current subarray we are focusing on
5        maxSum = -inf #Final return value, update it whenever we find a bigger subarray 
6
7        #Start from 2nd element since we used first element to initalize our variables 
8        for num in nums:
9            currSum = max(num, currSum + num)
10            maxSum = max(currSum, maxSum)
11        
12        return maxSum