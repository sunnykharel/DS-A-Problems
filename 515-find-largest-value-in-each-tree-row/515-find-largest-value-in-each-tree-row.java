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
    public List<Integer> largestValues(TreeNode root) {
        if ( root == null ) {
            return new ArrayList<Integer>();
        }
        List<TreeNode> prev = new ArrayList<>();
        prev.add(root);
        List<Integer> max = new ArrayList<>();
        
        while ( prev.size()>0 ){
            int max_val = prev.get(0).val;
            List<TreeNode> next = new ArrayList<>();
            for (TreeNode node : prev){
                max_val = Math.max(node.val, max_val);
                if (node.left != null)
                    next.add(node.left);
                if ( node.right!=null){
                    next.add(node.right);
                }
            }
            max.add(max_val);
            prev = next;
        }
        return max;
        
    }

}