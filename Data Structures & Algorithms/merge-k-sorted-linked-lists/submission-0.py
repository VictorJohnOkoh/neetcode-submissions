# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        if not lists:
            if len(lists) != 0:
                return lists
            else:
                return dummy.next


        i = 0
        j = i + 1
        while len(lists) > 1:
            list1, list2 = lists[i], lists[j]
            pointer = ListNode()
            tail = pointer
            while list1 and list2:
                if list1.val <= list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    list2 = list2.next
                pointer = pointer.next
            if list1:
                pointer.next = list1
            else:
                pointer.next = list2
            lists.append(tail.next)
            del lists[0]
            del lists[0]

        return lists[0]

