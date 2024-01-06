
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        ptr1 = first
        ptr2 = second
        str_num1 = ""
        str_num2 = ""
        
        while ptr1 is not None:
            str_num1+=str(ptr1.data)
            ptr1 = ptr1.next
            
        while ptr2 is not None:
            str_num2+=str(ptr2.data)
            ptr2 = ptr2.next
        
        str_result = str(int(str_num1) + int(str_num2))

        head = Node(0)
        curr = head
        count = 0
        while(count < len(str_result)):
            node = Node(str_result[count])
            curr.next = node
            count+=1
            curr = curr.next
        return head.next
            
        
        
        
        
        
        # code here
        # return head of sum list
