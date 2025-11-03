# Last updated: 11/2/2025, 8:23:25 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Iterative Approach 
        # Time Complexity: O(N), N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
        # Space Complexity: O(1)
        while True:
            # p, q are to the left of the root 
            if p.val > root.val and q.val > root.val:
                root = root.right
            # p, q are to the right of the root 
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else: # lca if p <= root <= q
                return root 

        """
        # Recursive Approach
        # Time Complexity: O(n)- N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
        # Space Complexity: O(n) - Naximum amount of space utilized by the recursion stack would be N since the height of a skewed BST could be N.

        # If both p and q are greater than root node
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        # If both p and q are less than root node
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        else:
            return root
        """


        
