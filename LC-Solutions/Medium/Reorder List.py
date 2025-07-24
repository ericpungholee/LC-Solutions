# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        sec = s.next
        prev = s.next = None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp

        first, sec = head, prev
        
        while sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1
            first, sec = tmp1, tmp2
