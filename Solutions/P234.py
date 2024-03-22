# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start=head
        l1=[]
        while start is not None:
            l1.append(start.val)
            start=start.next
        # print (l1)
        l2=l1[::-1]
        # print(l2)
        for i in range(len(l1)):
            if(l1[i]!=l2[i]):
                return False
        return True