# Last updated: 11/2/2025, 8:23:27 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True 

        first_half_end = self.end_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)      

        result = True 
        start = head
        middle = second_half_start
        while result and middle is not None:
            if start.val != middle.val:
                result = False 
            start = start.next
            middle = middle.next
        
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_first_half(self,head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow 


    def reverse_list(self,head):
        prev = None 
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 

        return prev
    