# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        new_head = head
        size  = 0
        new_tail = head
        while new_tail:
           size += 1
           if  new_tail.next is None:
               break
           new_tail = new_tail.next
        
        if size == k :
             return head
             
        count = 1
        while count < k and new_head:
            count +=1
            new_head = new_head.next
            
        tmp = new_head.next
        new_head.next = None
        

        new_tail.next = head
        
        head = tmp
        
        return head
