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
    public boolean isPalindrome(ListNode head) {
        //we get the int value of the number going forward, then going backwards as well
        //fails on lists with more that 10 elements (values too big)
        //we have to reverse the second half 
        if (head==null)
            return true;
        
        
        int length = 0;
        ListNode node = head;
        while (node!=null){
            length++; node=node.next;
        }
        
        ListNode right = head;
        for (int i = 0; i < length/2; i++, right=right.next){}
        if (length%2==1){
            right = right.next;
        }
        
        ListNode prev = null;
        ListNode next = right;
        while (next!=null){
            ListNode curr = next;
            next = curr.next;
            curr.next = prev;
            prev = curr;
        }
        
        for (int i = 0; i < length/2; i++, prev=prev.next, head=head.next){
            if (prev.val != head.val)
                return false;            
        }
        
        return true;
    }
}