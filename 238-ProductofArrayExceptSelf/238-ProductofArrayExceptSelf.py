# Last updated: 8/28/2026, 1:25:03 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        #answer is a list with default value of one that has same length as nums
4        answer = [1] * len(nums)
5
6        #left contains the product of all the element to the left 
7        left = 1 #prefix 
8        for i in range(len(nums)):
9            answer[i] = left
10            left *= nums[i]
11
12        #right contains the product of all the element to the right 
13        right = 1 #postfix 
14        for i in range(len(nums)-1, -1, -1): #could use reversed(range(length))
15            #For the index 'i', right would contain the product of all the elements to the right, and we update it accordingly 
16            answer[i] *= right
17            right *= nums[i]
18        
19        return answer 
20
21        #Time Complexity: O(n)
22        #Space Complexity: O(n)