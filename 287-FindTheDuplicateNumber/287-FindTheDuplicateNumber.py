# Last updated: 11/2/2025, 8:23:16 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Tortoise and Hare Algorithm, linked list cycle 
        slow = 0
        fast = 0

        #find the first intersection between fast and slow pointers 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #make a new pointer slow2 and find the intersection between slow and slow2 
        #that value is the duplicate value and the start of the linked list cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        #time complexity:O(n)
        #space complexity:O(1)
