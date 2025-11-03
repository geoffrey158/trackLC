// Last updated: 11/2/2025, 8:23:29 PM
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
    public TreeNode invertTree(TreeNode root) {

        //Recursion solution
        //Time complexity : O(n), cannot do better since at the very least we have to 
        //visit each node to invert it

        //Space complexity : O(n), where n is the height of the tree,
        //functions calls will be replaced on the stack in the worse case,

        //Base case to stop recursive calls 
        if(root == null){
            return null;
        }
        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;

        invertTree(root.left);
        invertTree(root.right);
        return root; 
    }
}