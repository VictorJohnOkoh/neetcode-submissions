# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = {}
        index = 0
        while head:
            if head in visited_nodes.values():
                return True
            else:
                index += 1
                visited_nodes[index] = head
            head = head.next

        return False
