#A stack is LIFO (Last in, First out)
#Like a stack of plates. You add plates to the top, and have to remove them first before you can get to the middle.

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return "Stack is empty"
    
    def peek(self):
        if len(self.items) > 0:
            return self.items [-1]
        else:
            return "Stack is empty"  

#Stack test set
my_Stack = Stack()
my_Stack.push("drew circle")
my_Stack.push("changed colour")
my_Stack.push("amended code")
my_Stack.push("pondered")
my_Stack.push("day dreamed")
print(my_Stack.items)
print(my_Stack.pop())
print(my_Stack.pop())
print(my_Stack.pop())
print(my_Stack.pop())
print(my_Stack.pop())
print(my_Stack.pop())