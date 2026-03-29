class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def prepend(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node

#Test cases
ll = LinkedList()
ll.append("cat")
ll.append("dog")
ll.append("fish")
ll.print_list()

print("---")
ll.prepend("hamster")
ll.print_list()