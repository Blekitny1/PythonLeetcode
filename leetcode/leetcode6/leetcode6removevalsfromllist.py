from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_vals_from_llist(self, head: Optional[ListNode], val_to_remove: int) -> Optional[ListNode]:
        previous = head
        next = head.next
        while next:
            if next.val == val_to_remove:
                previous.next = None
            else:
                previous.next = next
                previous = next
            next = next.next

        return previous if head.val != val_to_remove else None

    def remove_vals_from_llist_yt(self, head: Optional[ListNode], val_to_remove: int) -> Optional[ListNode]:
        dummy_head = ListNode(-2)
        dummy_head.next = head

        pointer = dummy_head
        while pointer.next:
            if pointer.next.val == val_to_remove:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return dummy_head.next


if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(3)
    node14 = ListNode(4)
    node11.next = node12
    node12.next = node13
    node13.next = node14

    node21 = ListNode(2)
    node22 = ListNode(2)
    node23 = ListNode(2)
    node24 = ListNode(2)
    node21.next = node22
    node22.next = node23
    node23.next = node24

    print(Solution().remove_vals_from_llist(node1, 5).val)
    print(Solution().remove_vals_from_llist(node11, 4).val)
    print(Solution().remove_vals_from_llist(node21, 2))
    print(Solution().remove_vals_from_llist_yt(node1, 5).val)
    print(Solution().remove_vals_from_llist_yt(node11, 4).val)
    print(Solution().remove_vals_from_llist_yt(node21, 2))

