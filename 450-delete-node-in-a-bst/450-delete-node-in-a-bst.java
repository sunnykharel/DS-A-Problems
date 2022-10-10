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
    public TreeNode deleteNode(TreeNode root, int key) {
        //first find the node
        //do a modified search, where when you encounter
        //the node you check the three cases
        if(root == null){
            return root;
        }
        else if( key>root.val){
            root.right=deleteNode(root.right, key);
        }
        else if(key<root.val){
            root.left=deleteNode(root.left, key);
        }
        else{
            if(root.left==null){
                root=root.right;
            }
            else if(root.right == null){
                root=root.left;
            }
            else{
                //get the min val in right subtree
                //recursively call delete--min val is a leaf
                int min_val= getMin(root.right);
                root.val=min_val;
                root.right=deleteNode(root.right, min_val);
            }
        }
        return root;
    }
    public int getMin(TreeNode root){
        if(root.left==null)
            return root.val;
        else
            return getMin(root.left);
    }
}