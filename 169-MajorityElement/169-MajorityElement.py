# Last updated: 12/23/2025, 7:35:34 AM
1class Solution:
2    def majorityElement(self, nums):
3        #Boyer–Moore Voting Algorithm
4        count = 0 #tracks balance of current candidate 
5        candidate = None #potential majority element
6
7        #iterate through each number in the array 
8        for num in nums:
9            # If count drops to 0, choose a new candidate, bc previous candidate has been cancelled out 
10            if count == 0:
11                candidate = num
12            
13            # if current number matches candidate, increase count
14            if num == candidate:
15                count += 1
16            # otherwise, cancel out one occurrence
17            else:
18                count -= 1
19
20        # since the problem guarantees a majority element,
21        # the remaining candidate must be the answer
22        return candidate
23
24        #Time Complexity:O(n),iterate through the array once per element
25        #Space Complexity:O(1)