// Last updated: 11/2/2025, 8:22:31 PM
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
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        // This will find the max depth going through each node,
        // and update the global maximum to the class member 'max'
        maxDepth(root);
        
        // Return the global maximum
        return max;
    
    }
    private int maxDepth(TreeNode root) {
        // Height of null is 0
        if (root == null) {
            return 0;
        }
        
        // Find height of left and right subTrees
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        
        // New global max is either already reached,
        // or is acheived using this node as the root
        max = Math.max(max, left + right);
        
        // Return height of tree rooted at this node
        return Math.max(left, right) + 1;
    }
        
    
}