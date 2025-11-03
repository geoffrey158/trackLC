// Last updated: 11/2/2025, 8:23:36 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
    
        //Iterative Approach 
        //Time complexity : O(n)
        //Space complexity : O(1)

        
        ListNode prev = null; //used to point to previous node
        ListNode curr = head; //used to point to current node 
    
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
        

        //Recursive Approach
        //Time complexity : O(n) 
        //Space complexity: O(n), The extra space comes from implicit stack space due to recursion.  
        //The recursion could go up to n levels deep.
        /*
        if (head == null || head.next == null) {
            return head;
        }
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;
        */
    }
}