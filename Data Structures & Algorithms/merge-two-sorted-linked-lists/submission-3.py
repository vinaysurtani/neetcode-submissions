# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = LL = ListNode()

        if list1 is None:
            return list2
        if list2 is None:
            return list1        
        while list1 and list2:
            if list1.val <= list2.val:
                LL.next = list1
                list1 = list1.next
            else:
                LL.next = list2
                list2 = list2.next
            LL = LL.next
        while list1 is not None:
            LL.next = list1
            list1 = list1.next
            LL = LL.next
        while list2 is not None:
            LL.next = list2
            list2 = list2.next
            LL = LL.next
        return dummy.next