class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.data < list2.data:
            current.bottom = list1
            list1 = list1.bottom
        else:
            current.bottom = list2
            list2 = list2.bottom

        current = current.bottom

    if list1:
        current.bottom = list1
    else:
        current.bottom = list2

    return dummy.bottom

def flatten(root):
    if not root or not root.next:
        return root

    root.next = flatten(root.next)
    root = merge_sorted_lists(root, root.next)

    return root
