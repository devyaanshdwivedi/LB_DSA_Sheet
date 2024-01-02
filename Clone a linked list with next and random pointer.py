#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
''' 
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        if not head:
            return None
        
        original_to_copy = {}  
        
        current = head
        while current:
            original_to_copy[current] = Node(current.data)
            current = current.next
        
        current = head
        while current:
            if current.next:
                original_to_copy[current].next = original_to_copy[current.next]
            if current.arb:
                original_to_copy[current].arb = original_to_copy[current.arb]
            current = current.next
        
        return original_to_copy[head]