#User function Template for python3
import heapq

'''
    Your task is to merge the given k sorted
    linked lists into one list and return
    the the new formed linked list class.

    Function Arguments:
        arr is a list containing the n linkedlist head pointers
        n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
        
'''
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        # return head of merged list
        
        minh=[]
        
        for i in range(K):
            heapq.heappush(minh, (arr[i].data, i, arr[i]))
            
        head=Node(-1)
        tail=head
        
        while minh:
            data, i, temp=heapq.heappop(minh)
            tail.next=temp
            tail=tail.next
            
            if temp.next:
                heapq.heappush(minh, (temp.next.data, i, temp.next))


        return head.next                
            
