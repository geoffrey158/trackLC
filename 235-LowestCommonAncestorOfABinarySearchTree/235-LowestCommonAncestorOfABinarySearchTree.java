// Last updated: 11/2/2025, 8:23:26 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){
            return null;
        }
        if(p.val<=root.val && q.val>=root.val || q.val<=root.val && p.val>=root.val){
            return root;
        }
        else if(p.val < root.val && q.val < root.val){
            return lowestCommonAncestor(root.left,p,q);
        }
        else{
            return lowestCommonAncestor(root.right,p,q);

        }

        //Time Complexity:O(N)
        //Space Complexity:O(N)
    }
}