# Last updated: 11/2/2025, 8:22:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxVal = 0 #Store the length of the diameter of the tree

        def dfs(root):
            nonlocal maxVal #Allows modification of maxVal from the outer scope

            #Base case
            if root is None:
                return 0
            
            #Recursively find the height of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right) 

            #Update the max diameter at this node if it's greater than current max
            maxVal = max(maxVal,left+right) #left+right is the diameter through the current node

            return max(left,right) + 1 #Height = max of left/right subtree + 1 for current node

        dfs(root)
        return maxVal

        #Time Complexity: On(n). Recursion function maxdepth, we enter and exit from each node once
        #Space Complexity: O(h)
        #n is the number of nodes and h is the height of the tree
        
            
        