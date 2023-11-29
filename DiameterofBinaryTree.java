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
    public int diameterOfBinaryTree(TreeNode root) {
        int res[] = {0};
        diameterOfBT(root, res);
        return res[0];
    }
    public int diameterOfBT(TreeNode root, int[] res){
        if(root == null){
            return 0;
        }
        int left = 0;
        int right = 0;
        left = diameterOfBT(root.left, res);
        right = diameterOfBT(root.right, res);
        res[0] = Math.max(res[0], left+right);
        return Math.max(left, right) + 1;
    }
}