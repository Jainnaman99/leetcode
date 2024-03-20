# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start=list1
        # ptr=list1
        for _ in range(a-1):
            start=start.next
        # print(start)
        ptr=start.next
        for _ in range(b-a+1):
            ptr=ptr.next
        start.next=list2
        while list2.next:
            list2=list2.next
        list2.next=ptr
        # print(list2)
        return list1