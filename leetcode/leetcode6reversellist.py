from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverse_llist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        result = None
        while pointer:
            next_pointer = pointer.next
            pointer.next = result
            
            result = pointer
            pointer = next_pointer

        return result


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
    print(Solution().reverse_llist(node1).val)
    print(Solution().reverse_llist(node11).val)

