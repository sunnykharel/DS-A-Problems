/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode node = head;
        ListNode prev = null;
        while (node!=null){
            
            int curr_val = node.val;
            ListNode newNext = node.next;
            int currCount = 1;
            while(newNext!=null && newNext.val == curr_val){
                newNext = newNext.next;
                currCount++;
            }
            
            if (currCount>1){
                if (prev == null){
                    head = newNext;
                }else{
                    prev.next = newNext;
                }
            }else{
                prev = node;
            }
            
            node = newNext;
        
        }
        return head;
        
    }
}