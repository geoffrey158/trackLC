# Last updated: 1/9/2026, 7:45:50 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        #Floyd's Tortoise and Hare Algorithm, linked list cycle 
4        slow = 0
5        fast = 0
6
7        #find the first intersection between fast and slow pointers 
8        while True:
9            slow = nums[slow]
10            fast = nums[nums[fast]]
11            if slow == fast:
12                break
13
14        #make a new pointer slow2 and find the intersection between slow and slow2 
15        #that value is the duplicate value and the start of the linked list cycle
16        slow2 = 0
17        while True:
18            slow = nums[slow]
19            slow2 = nums[slow2]
20            if slow == slow2:
21                return slow
22
23        #time complexity:O(n)
24        #space complexity:O(1)
25