// Last updated: 11/2/2025, 8:22:27 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
     public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (isSame(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }
    
    private boolean isSame(TreeNode root, TreeNode subRoot) {
        //first condition 
        if (root == null && subRoot == null) return true;
        
        //second condition
        // equivalent of (s == null && t != null) || (s != null) && (t==null)
        if (root == null || subRoot == null) return false;
        
        //third conition
        if (root.val != subRoot.val) return false;
        
        return isSame(root.left, subRoot.left) && isSame(root.right, subRoot.right);
    }
}