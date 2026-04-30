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
    public ListNode reverseList(ListNode head) {
        ListNode ptr = head, curr = head, prev = null;
        if (ptr != null){ptr = ptr.next;} 
        else { return head;}
        while (ptr != null){
            curr.next = prev;
            prev = curr;
            curr = ptr;
            ptr = ptr.next;
        }
        curr.next = prev;
        return curr;
    }
}
