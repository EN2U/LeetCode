# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
#


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list_node = ListNode(val=(l1.val + l2.val) % 10, next=None)

        current_node = new_list_node

        value = int((l1.val + l2.val) / 10)

        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                value += l1.val

            if l2.next:
                l2 = l2.next
                value += l2.val

            current_node.next = ListNode(val=value % 10, next=None)

            current_node = current_node.next

            value = int(value / 10)

        if value != 0:
            current_node.next = ListNode(val=value, next=None)

        return new_list_node
