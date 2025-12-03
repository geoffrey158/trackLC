# Last updated: 12/3/2025, 5:55:46 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9        curr = head
10        prev = None
11
12        while curr:
13
14            temp = curr.next
15            curr.next = prev
16            prev = curr
17            curr = temp
18
19        return prev
20             