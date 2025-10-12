from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


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
    node14.next = node12
    print(Solution().hasCycle(node1))
    print(Solution().hasCycle(node11))

