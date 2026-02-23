# Last updated: 2/23/2026, 4:27:05 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow = head
10        fast = head
11
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15
16            #if the pointers meet that means there is a cycle
17            if slow == fast:
18                return True
19
20        
21        return False