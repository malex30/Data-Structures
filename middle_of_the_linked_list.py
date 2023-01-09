# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head)
            head = head.next
        return temp[len(temp)//2]

# time complexity o(n) because I interate through each index of one temp array
# space complexity o(1) because no new data structure is proportionally created