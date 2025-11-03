# Last updated: 11/2/2025, 8:22:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return False

        if self.isSameTree(root,subRoot):
            return True 

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self, root,subRoot):
        if root == None and subRoot == None:
            return True  

        if root == None or subRoot == None:
            return False
        
        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)


        