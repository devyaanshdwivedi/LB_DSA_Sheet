"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        curr = head
        prev = None
        count = 0
        while curr and count<k:
            following = curr.next
            curr.next = prev
            prev = curr
            curr = following
            count += 1
        if curr is not None:
            head.next = self.reverse(curr,k)
        return prev
        