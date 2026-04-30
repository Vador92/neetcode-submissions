# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first, sec = list1, list2
        head, ans = ListNode(), ListNode()
        head.next = ans
        while first is not None and sec is not None:
            if first.val <= sec.val:
                ans.next = first
                ans = ans.next
                first = first.next
            else:
                ans.next = sec
                ans = ans.next
                sec = sec.next
        
        if first is not None:
            ans.next = first
        else:
            ans.next = sec
        return head.next.next