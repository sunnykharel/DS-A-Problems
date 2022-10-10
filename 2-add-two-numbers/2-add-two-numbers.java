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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int pow10 = 1;
        ListNode node = new ListNode();
        ListNode head = node;
        
        int c = 0;
        while (l1!=null && l2!=null){
            int sum = l1.val+l2.val+c;
            node.next = new ListNode(sum%10);
            c = sum/10;
            node = node.next;
            l1=l1.next;l2=l2.next;
        }
        if (l1!=null || l2!=null){
            ListNode remain = l1==null ? l2 : l1;
            while (remain!=null){
                int sum = remain.val+c;
                node.next = new ListNode(sum%10);
                c = sum/10;
                node = node.next;
                remain=remain.next;
            }
        }
        if (c!=0){
            node.next = new ListNode(c);
        }
        return head.next;
        
        
    }
}