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
    private List<List<Integer>> levelOrder;
    public List<List<Integer>> levelOrder(TreeNode root) {
        levelOrder = new ArrayList<List<Integer>>();
        dfsLevelOrder(0, root);
        return levelOrder;
    }
    private void dfsLevelOrder(int depth, TreeNode root){
        if(root==null)
            return;
        if(levelOrder.size()<=depth){
            levelOrder.add(new ArrayList<Integer>());
        }
        levelOrder.get(depth).add(root.val);
        dfsLevelOrder(depth+1, root.left);
        dfsLevelOrder(depth+1, root.right);
    }
}