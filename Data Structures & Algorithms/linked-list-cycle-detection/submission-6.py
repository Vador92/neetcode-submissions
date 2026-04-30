# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        if fast is None or fast.next is None:
            return False
        fast = fast.next
        fast = fast.next
        while fast is not None:
            print("here")
            if slow == fast:
                return True
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            
        return False

